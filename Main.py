import discord
from discord.ext import commands
import asyncio
import random

description = ''' A bot for the Krosmaga Discord Server. Nice features incoming !'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def card(ctx, *, card_name : str):
    card_name_lower = card_name.lower();
    card_path = "./Cards/" + card_name_lower.replace(" ", "_") + ".png";
    try:
        await bot.send_file(ctx.message.channel , card_path)
    except FileNotFoundError:
       await bot.say("Oups cette carte n'existe pas")

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

bot.run('MjMzOTYyMDkzODE1MTM2MjU2.Ct5nwA.HNZfuT67-jTc8CZqhyRT9F-5XN8')

