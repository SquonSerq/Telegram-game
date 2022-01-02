from telegram import Update, bot, update
from telegram.ext import Updater, CallbackContext, CommandHandler
import json

from utils.game_queue import create_room

def main():
	with open('config.json') as bot_config:
		config_data = json.load(bot_config)

	updater = Updater(config_data['token'], use_context=True)
	dispatcher = updater.dispatcher

	create_room_handler = CommandHandler('createroom', create_room)
	dispatcher.add_handler(create_room_handler)

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	main()