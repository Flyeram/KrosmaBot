from discord.ext import commands
import requests
import os
import copy
import shutil
import asyncio

class ROLE:
	"""Utilities that manages roles."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def role(self, ctx):
		"""Commands to manage roles"""
		if ctx.invoked_subcommand is None:
				msg = await self.bot.say('Incorrect random subcommand passed.')
				await asyncio.sleep(3)
				await self.bot.delete_message(msg)

	@role.command()
	async def show(self):
		pass

def setup(bot):
	bot.add_cog(ROLE(bot))