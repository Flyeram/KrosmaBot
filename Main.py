import discord
from discord.ext import commands
from cogs.Utils.checkUtils import *
from cogs.Utils.MessageUtils import *
import asyncio
import sys
import json
import os
import cogs.lk

initial_extensions = [
	'cogs.card',
	'cogs.role',
	'cogs.trivia',
	'cogs.lk'
]

description = ''' A bot for the Krosmaga Discord Server. Nice features incoming !'''
bot = commands.Bot(command_prefix='?', description=description)
if (sys.argv[1] == "debug"):
	RELEASE = False
else:
	RELEASE = True

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.event
async def on_member_join(member):
	servers = list(bot.servers)
	if (member.server.name == "Krosmaga Communaute"):
		roles = member.server.roles
		for i in range(len(roles)):
			if (roles[i].name == "Krosmage"):
				role = roles[i]
		await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def bracket(ctx):
	ctx.message.content = "?lk bracket"
	await bot.process_commands(ctx.message)
	

if __name__ == '__main__':

	RELEASE = False

	if (sys.argv[1] == "debug"):
		#Beta run
		with open(os.getcwd() + "\\res\\settings.json", encoding="utf_8_sig") as data_file:
			data = json.load(data_file)
		token = data["DebugToken"]
	else:
		#Official run
		with open(os.getcwd() + "/res/settings.json", encoding="utf_8_sig") as data_file:
			data = json.load(data_file)
		token = data["ReleaseToken"]

	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
	bot.run(token)

