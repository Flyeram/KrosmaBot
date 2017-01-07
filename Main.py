import discord
from discord.ext import commands
from cogs.Utils.checkUtils import *
from cogs.Utils.MessageUtils import *
import asyncio

initial_extensions = [
	'cogs.card',
	'cogs.role',
	'cogs.trivia'
]


description = ''' A bot for the Krosmaga Discord Server. Nice features incoming !'''
bot = commands.Bot(command_prefix='?', description=description)

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

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

	bot.run('MjMzOTYyMDkzODE1MTM2MjU2.Ct5nwA.HNZfuT67-jTc8CZqhyRT9F-5XN8')

