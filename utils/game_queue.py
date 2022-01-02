from telegram import Update
from telegram.ext import CallbackContext
from models.game_queue_handler import Game_room_handler

roll_rooms = Game_room_handler()

def create_room(update: Update, context: CallbackContext):
	chat_id = update.effective_chat.id

	for i in range(0, 100):
		roll_rooms.create_room(chat_id+i, i)

	rooms = roll_rooms.get_rooms(1)

	answer = ""

	for i in rooms:
		answer += f"\n{i}"

	update.message.reply_text(answer)

	