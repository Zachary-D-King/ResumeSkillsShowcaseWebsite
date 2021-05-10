from datetime import datetime

class MessageAdd:
	
	#Initialize a variable that identifies the number it is on for later
	messageId = 0

	# Initializing class
	def __init__(self, message):
		self.message = message
		self.datetime = datetime.now()
		self.messageId = MessageAdd.messageId
		MessageAdd.messageId += 1
		# This homework helper is going to only use messages, since it should help the user with managing homework. 
		#TODO (optional) firebase realtime database to manage homework with other users

	# Return a string to post to list
	def __str__(self):
		return self.message + "--" + self.datetime.__str__()

	def set_message(self, message):
		self.message = message

	def get_message_id(self):
		return self.messageId


