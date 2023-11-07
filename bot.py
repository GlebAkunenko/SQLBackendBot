class User:
	def __init__(self):
		self.state = 0


import config, json

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

bot = AsyncTeleBot(config.token)
users: dict[int, User] = {}


def with_state(n):
	def _check(message: Message) -> bool:
		user_id = message.from_user.id
		if user_id not in users:
			return False
		return users[user_id].state == n
	return _check


def with_states(states: tuple):
	def _check(message: Message) -> bool:
		user_id = message.from_user.id
		if user_id not in users:
			return False
		return users[user_id].state in states
	return _check


@bot.message_handler(commands='start')
async def start(message: Message):
	users[message.from_user.id] = User()
	await bot.send_message(message.from_user.id, "Hi")


# @bot.message_handler(func=with_state(0))
async def state0(message: Message):
	user = users[message.from_user.id]
	await bot.send_message(message.from_user.id, "you state is 1 now")
	user.state = 1


@bot.message_handler(func=with_state(1))
async def state1(message: Message):
	user = users[message.from_user.id]
	await bot.send_message(message.from_user.id, "you state is 0 now")
	user.state = 0


import asyncio
print("Bot started")
asyncio.run(bot.infinity_polling())