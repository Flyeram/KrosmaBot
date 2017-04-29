import discord
from discord.ext import commands
import asyncio

async def BotSayError(bot, channel, message):
	await BotSay(bot, channel, message, 3)

async def BotSay(bot, channel, message, time):
	msg = await bot.send_message(channel, message)
	await asyncio.sleep(time)
	await bot.delete_message(msg)