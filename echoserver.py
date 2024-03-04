# Packages
import logging #화면에 로그를 보여주기 위함
from telegram import Update #사용자가 텔레그램 서버에서 메세지 받을 때의 데이터
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext #텔레그램 확장 서비스 제공
# Enable logging
logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
) #INFO를 로깅하는 format을 제공하여 출력

logger = logging.getLogger(__name__) # 해당 파일의 로그를 받아서 그려줘라.

# Message Handlers 3가지
def start(update: Update, context: CallbackContext) -> None:
    """send a message when the command /start is issued."""
    update.message.reply_text('start')
    print(update.message.chat_id) # 유저 저장(chatid로 보낸다.)
    # 1854165413

def help_command(update: Update, context: CallbackContext) -> None:
    """send a message when the command /help is issued."""
    update.message.reply_text('Help!') #helf시에 데이터를 보여주는 것

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text) #echoserver 생성(사용자가 입력한 데이터를 보내줌)

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
    updater = Updater("YOUR TOKEN") #token 가져오기

    #updater.bot.send_message(your_chat_id, "cbchoi_bot started")

    # 핸들러를 등록하기 위해 디스패처를 가져온다.
    dispatcher = updater.dispatcher 
    # 다른 명령에 대해서 Telegram이 답변
    dispatcher.add_handler(CommandHandler("start", start)) #start끼리 연결하라 (디스패쳐와 핸들러)
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("calc", calc1))
    
    # 메세지와 커맨드를 빼고 텔레그램에 메시지를 에코처리.
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
     # Start the Bot
    updater.start_polling() #백그라운드에서 블로킹하기 위에 idle까지 쓴다.(잠깐 멈춰주게)
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
