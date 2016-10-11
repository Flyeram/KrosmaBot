import discord
from discord.ext import commands
import asyncio

description = '''An example bot to showcase the discord.ext.commands extension
module. '''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def card(ctx, card_name : str):
    card_path = "./Cards/" + card_name + ".jpg";
    try:
        await bot.send_file(ctx.message.channel , card_path)
    except FileNotFoundError:
       await bot.say("Oups cette carte n'existe pas")

bot.run('MjMzOTYyMDkzODE1MTM2MjU2.Ct5nwA.HNZfuT67-jTc8CZqhyRT9F-5XN8')

