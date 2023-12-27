# Packages
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# Enable logging
logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Message Handlers
def start(update: Update, context: CallbackContext) -> None:
    """send a message when the command /start is issued."""
    update.message.reply_text('start')
    print(update.message.chat_id)
    # 1854165413

def help_command(update: Update, context: CallbackContext) -> None:
    """send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def calc1(update: Update, context: CallbackContext) -> None:
    print(update.message.text)
    tokens = update.message.text.split(' ')
    arg1 = int(tokens[1])
    op   = tokens[2]
    arg2 = int(tokens[3])

    if op == '+':
        update.message.reply_text(f'{arg1 + arg2}')
    elif op == '-':
        update.message.reply_text(f'{arg1 - arg2}')
    elif op == '*':
        update.message.reply_text(f'{arg1 * arg2}')
    elif op == '/':
        update.message.reply_text(f'{arg1 / arg2}')
    elif op == '^':
        update.message.reply_text(f'{arg1 ^ arg2}')
    pass

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("YOUR TOKEN")

    #updater.bot.send_message(your_chat_id, "cbchoi_bot started")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("calc", calc1))
    
    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
     # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    # 1. Handler를 추가 : calcuation, cmd: /calc
    # 2. 사용자로부터 메시지를 받아서 Parsing, update.message.text
    # 2.1. 첫번째 숫자 + 두번째 숫자, split함수를 활용
    # 2.2. 첫번째 숫자 - 두번째 숫자, split함수를 활용
    # 2.3. 첫번째 숫자 * 두번째 숫자, split함수를 활용
    # 2.4. 첫번째 숫자 / 두번째 숫자, split함수를 활용
    # 2.5. 첫번째 숫자 ^ 두번째 숫자, split함수를 활용, 2 ^ 3 = 8
    # 3. 결과를 사용자에게 반환 update.message.reply_text()
    
if __name__ == '__main__':
    main()
