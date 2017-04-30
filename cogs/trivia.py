from discord.ext import commands
from .Utils.checkUtils import *
from .Utils.MessageUtils import *
import random

class TRIVIA:
	"""Commands you don't know where they belong"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def tr(self, ctx):
		"""Commands that are not repertoried, and has very differents purposes"""
		if ctx.invoked_subcommand is None:
			await BotSayError(self.bot, ctx.message.channel, "Incorect trivia subcommand passed")

	@tr.command()
	async def test(self):
		""" Commande pour quand il y a besoin de tester des trucs, inutiles donc pour vous desole"""
		await self.bot.say("Commande de test disable")
	
	@tr.command(pass_context=True)
	async def roll(self, ctx, dice : str):
		"""Rolls a dice in NdN format."""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await BotSayError(self.bot, ctx.message.channel, "Format has to be NdN !")
			return

		if (limit > 9999):
			limit = 9999
		if (rolls > 50):
			rolls = 50
		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await self.bot.say(result)

	@tr.command(description='For when you wanna settle the score some other way')
	async def choose(self, *choices : str):
		"""Chooses between multiple choices."""
		await self.bot.say(random.choice(choices))

	@tr.command(pass_context=True)
	async def talk(self, ctx, destination,*,message : str):
		try:
			await self.bot.delete_message(ctx.message)
		except:
			pass
		member = ctx.message.author
		if not(checkMemberRole(member, "Admin")):
			return
		try:
			await self.bot.send_message(getChannelByName(self.bot, ctx.message.server, destination), message)
		except:
			await BotSayError(self.bot, ctx.message.channel, "Message Failed")

def setup(bot):
	bot.add_cog(TRIVIA(bot))