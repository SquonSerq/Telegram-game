class Game_room_handler:
	def __init__(self):
		self.room = {}

	def create_room(self, chat_id, amount):
		if chat_id not in self.room:
			self.room[chat_id] = amount
			return True
		else:
			return False

	def remove_room(self, chat_id):
		if chat_id in self.room:
			self.room.pop[chat_id]

	def get_rooms(self, offset: int):
		offset_rooms = []
		j = -1
				
		for chat_id, v in self.room.items():
			j+=1
			if j < offset:
				continue
			
			if len(offset_rooms) == 10:
				return offset_rooms

			len(offset_rooms)
			offset_rooms.append(v)

