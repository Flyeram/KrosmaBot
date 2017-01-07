from discord.ext import commands
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
		"""Display requested cards"""
		if ctx.invoked_subcommand is None:
				msg = await self.bot.say('Incorrect card subcommand passed.')
				await asyncio.sleep(3)
				await self.bot.delete_message(msg)

	@card.command(pass_context=True)
	async def show(self, ctx, *, card_name : str):
		""" Link la carte passe en parametre
		pour les infinites il faut rajouter 1, 2 ou 3 derriere le nom pour les formes"""
		card_name_lower = card_name.lower();
		card_name_replace = card_name_lower.replace(" ", "_")
		test_infinite = card_name_replace[-2:]
		if test_infinite in ["_1", "_2", "_3"]:
			card_path = card_name_replace.replace(test_infinite, "_niveau" + test_infinite) + ".png";
		else:
			card_path = card_name_replace + ".png";
		try:
			r = requests.get("http://vps326325.ovh.net/Cards/" + card_path, stream=True)
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
			msg = await self.bot.send_message(ctx.message.channel, "Oups cette carte n'existe pas")
			await asyncio.sleep(3)
			await self.bot.delete_message(msg)
		except OSError:
			pass

def setup(bot):
	bot.add_cog(CARD(bot))


