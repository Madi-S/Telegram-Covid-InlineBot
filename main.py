from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, InlineQueryHandler, Filters, CallbackContext

from config import TG_TOKEN
from stats import get_stats
from searcher import Searcher

from uuid import uuid4
from get_loggers import get_logger


s = Searcher()
logger = get_logger()


def debug_requests(f):
    def inner(*args, **kwargs):
        try:
            logger.info('Method %s called', f.__name__)
            return f(*args, **kwargs)
        except Exception:
            logger.exception('Error in handler %s', f.__name__)
            raise

    return inner


@debug_requests
def inline_callback(update: Update, context: CallbackContext):
    query = update.inline_query.query.strip().lower()

    logger.info('Query received: %s', query)

    results = []

    for country in s.countries:
        if (query in country.lower() and len(query) >= 2) or query == country.lower():
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=country,
                    input_message_content=InputTextMessageContent(
                        get_stats(country))
                ))

    update.inline_query.answer(results)

    update.inline_query.answer(
        results=results,
        cache_time=120,
    )


@debug_requests
def msg_callback(update: Update, context: CallbackContext):
    if not update.message:
        return
    update.message.reply_text(
        text=f'There is nothing in this chat\n\nMove to another chat and start typing my name @{update.message.bot.username}',
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    logger.info('Bot Started')

    updater = Updater(TG_TOKEN, use_context=True)
    dp = updater.dispatcher

    logger.info(updater.bot.get_me())

    dp.add_handler(InlineQueryHandler(inline_callback))
    dp.add_handler(MessageHandler(filters=Filters.all, callback=msg_callback))

    updater.start_polling()
    updater.idle()

    logger.info('Bot Finished')


if __name__ == "__main__":
    main()
