from discord.ext import commands
from .Utils.checkUtils import *
from .Utils.MessageUtils import *
from .Utils.miscUtils import *
import requests
import os
import copy
import shutil
import asyncio
import pickle

class LK:
	"""Utilities that manages roles."""

	def __init__(self, bot):
		self.bot = bot
		self.links = {}
		self.path = os.getcwd() + "\\res\\lk.pkl"
		self.links = load_obj(self.path)

	@commands.group(pass_context=True)
	async def lk(self, ctx):
		"""Commands to create link as runtime"""
		try:
			await self.bot.delete_message(ctx.message)
		except:
			pass
		name = ctx.message.content
		name = name[4:]
		if name in self.links:
			await BotSay(self.bot, ctx.message.channel, self.links[name], 60)
		elif ctx.invoked_subcommand is None:
			await BotSayError(self.bot, ctx.message.channel, "Incorect lk subcommand passed")

	@lk.command(pass_context = True)
	async def add(self, ctx, name = None,*, text : str = None):
		""" Command that add a LK with a name and a description"""
		try:
			await self.bot.delete_message(ctx.message)
		except:
			pass

		if not(checkMembersRoles(ctx.message.author, ['Admin', 'test'])):
			await BotSayError(self.bot, ctx.message.channel, "You do not have the permission to use this command")
			return
		if (name == None or str == None):
			await BotSayError(self.bot, ctx.message.channel, "Missing argument for this command")
			return
		if (name == 'add' or name == 'remove' or name == 'show'):
			await BotSayError(self.bot, ctx.message.channel, "You cannot use this name")
			return
		if (name in self.links):
			await BotSayError(self.bot, ctx.message.channel, "LK with name [" + name + "] already exist, please remove it before remplacing it")
			return

		self.links[name] = text;
		save_obj(self.links, self.path)
		await BotSayError(self.bot, ctx.message.channel, "LK [" + name + "] with description [" + text + "] was successfully added")
	
	@lk.command(pass_context = True)
	async def remove(self, ctx, name = None):
		"""Command that removes a LK with his name"""
		try:
			await self.bot.delete_message(ctx.message)
		except:
			pass

		if not(checkMembersRoles(ctx.message.author, ['Admin', 'test'])):
			await BotSayError(self.bot, ctx.message.channel, "You do not have the permission to use this command")
			return
		if (name == None):
			await BotSayError(self.bot, ctx.message.channel, "Missing argument for this command")
			return
		if not(name in self.links):
			await BotSayError(self.bot, ctx.message.channel, "LK with name [" + name + "] doesn't exist")
			return

		del self.links[name]
		save_obj(self.links, self.path)
		await BotSayError(self.bot, ctx.message.channel, "LK [" + name + "] was successfully removed")

	@lk.command(pass_context = True)
	async def show(self, ctx):
		"""Command that shows all LK available"""
		try:
			await self.bot.delete_message(ctx.message)
		except:
			pass
		
		message = "```~~ LK currently available ~~\n\n"
		for key in self.links:
			message += "- [" + key + "]\n"
		message += "```"
		await BotSay(self.bot, ctx.message.channel, message, 60)



def setup(bot):
	bot.add_cog(LK(bot))