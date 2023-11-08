class User:
	def __init__(self):
		self.state = 0


import config, json

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from model import do_query
from prettytable import PrettyTable

bot = AsyncTeleBot(config.token)


@bot.message_handler(commands='start')
async def start(message: Message):
	await bot.send_message(message.from_user.id, config.hello)


@bot.message_handler(func=lambda x: True)
async def handler(message: Message):
	await bot.send_message(message.from_user.id, "<code>" + make_request(message.text) + "</code>", parse_mode='html')


def make_request(query: str) -> str:
	try:
		data = do_query(query)
	except:
		return "Invalid SQL query"
	if len(data) == 0:
		return "No data"
	pt = PrettyTable([str(i) for i in range(len(data[0]))])
	pt.add_rows(data)
	return str(pt)




import asyncio
print("Bot started")
asyncio.run(bot.infinity_polling())

