from loguru import logger
from loader import bot
from states.user_states import UserState
from telebot.types import ReplyKeyboardRemove


@logger.catch()
def finish_work(user_id: int, chat_id: int) -> None:
    logger.info('Завершение выполнение команды')
    bot.set_state(user_id, UserState.finish, chat_id)
    bot.send_message(user_id, 'Закончил выполнение команды')
