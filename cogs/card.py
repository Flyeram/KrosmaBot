from discord.ext import commands
from .Utils.checkUtils import *
from .Utils.MessageUtils import *
import requests
import os
import copy
import shutil
import asyncio

class CARD:
	"""Card class commands"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def card(self, ctx):
		"""Command group about cards, for now you can only display cards"""
		if ctx.invoked_subcommand is None:
			await BotSayError(self.bot, ctx.message.channel, "Incorect card subcommand passed")

	@card.command(pass_context=True)
	async def show(self, ctx, lang = "fr",*, card_name : str):
		""" Link the card named
		format has to be : "?card show langue card_name"
		To display infinites cards you have to add the number 1, 2, 3 after the name and a space
		exemples :
		?card show en tronknyde
		?card show fr amalia 3"""
		card_name_lower = card_name.lower();
		card_name_replace = card_name_lower.replace(" ", "_")
		test_infinite = card_name_replace[-2:]
		if test_infinite in ["_1", "_2", "_3"]:
			card_path = card_name_replace.replace(test_infinite, "_niveau" + test_infinite) + ".png";
		else:
			card_path = card_name_replace + ".png";
		try:
			partA = "vps"
			partB = "326"
			partC = "325"
			partD = ".ovh.net/"
			r = requests.get("http://" + partA + partB + partC + partD + "Cards_" + lang + "/" + card_path, stream=True)
			if r.status_code == 200:
				with open("./" + card_path, 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw, f)
			try:
				await self.bot.delete_message(ctx.message)
			except:
				pass
			msg = await self.bot.send_file(ctx.message.channel , "./" + card_path)
			os.remove("./" + card_path)
			await asyncio.sleep(60)
			await self.bot.delete_message(msg)
		except FileNotFoundError:
			await BotSayError(self.bot, ctx.message.channel, "Oups, this card doesn't exist !")
		except OSError:
			pass

def setup(bot):
	bot.add_cog(CARD(bot))


