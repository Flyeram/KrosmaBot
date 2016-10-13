import discord
from discord.ext import commands
import asyncio
import random
import copy

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
    if (member.server.name == "Krosmaga Communaute FR"):
        roles = member.server.roles
        for i in range(len(roles)):
            if (roles[i].name == "Krosmagien"):
                role = roles[i]
        await bot.add_roles(member, role)

@bot.command()
async def test():
    """ Commande pour quand il y a besoin de tester des trucs, inutiles donc pour vous desole"""
    await bot.say("Commande de test disable")


@bot.command(pass_context=True)
async def card(ctx, *, card_name : str):
    """ Link la carte passe en parametre
    pour les infinites il faut rajouter 2 ou 3 derriere le nom pour les autre formes"""
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

