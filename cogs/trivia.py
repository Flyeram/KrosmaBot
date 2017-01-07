from discord.ext import commands
import random

class TRIVIA:
	"""Commands you don't know where they belong"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def trivia(self, ctx):
		"""Useless commands"""
		if ctx.invoked_subcommand is None:
				await self.bot.say('Incorrect trivia subcommand passed.')

	@trivia.command()
	async def test(self):
		""" Commande pour quand il y a besoin de tester des trucs, inutiles donc pour vous desole"""
		await self.bot.say("Commande de test disable")
	
	
	@trivia.command()
	async def roll(self, dice : str):
		"""Rolls a dice in NdN format."""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await self.bot.say('Format has to be in NdN!')
			return

		if (limit > 9999):
			limit = 9999
		if (rolls > 50):
			rolls = 50
		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await self.bot.say(result)

	@trivia.command(description='For when you wanna settle the score some other way')
	async def choose(self, *choices : str):
		"""Chooses between multiple choices."""
		await self.bot.say(random.choice(choices))

def setup(bot):
	bot.add_cog(TRIVIA(bot))