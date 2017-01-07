import discord
from discord.ext import commands
import asyncio

async def BotSayError(bot, channel, message):
	msg = await bot.send_message(channel, message)
	await asyncio.sleep(3)
	await bot.delete_message(msg)