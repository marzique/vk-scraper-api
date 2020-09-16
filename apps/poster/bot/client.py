import logging

import telegram
from telegram.ext import Updater
from telegram.constants import MAX_MESSAGE_LENGTH

from config.settings import TELEGRAM_TOKEN


class TelegramClient:
    CHAT_ID = '@ArsenalRepostsTest'  # channel name where messages will be sent

    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_TOKEN)

    def send_message(self, text='', parse_mode='HTML'):
        try:
            return self.bot.send_message(
                chat_id=self.CHAT_ID, 
                text=text, 
                parse_mode=parse_mode
            )
        except telegram.error.BadRequest:
            return False

