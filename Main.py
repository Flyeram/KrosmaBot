import discord
from discord.ext import commands
import asyncio
import random
import copy
import time
import requests
import shutil
import os

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
    print("member joined")
    servers = list(bot.servers)
    if (member.server.name == "Krosmaga Communaute FR"):
        print("joined Krosmaga")
        roles = member.server.roles
        for i in range(len(roles)):
            if (roles[i].name == "Krosmagien"):
                print("Krosmagien found")
                role = roles[i]
        await bot.add_roles(member, role)

@bot.command()
async def test():
    """ Commande pour quand il y a besoin de tester des trucs, inutiles donc pour vous desole"""
#await bot.say("Commande de test disable")
    
    
@bot.command(pass_context=True)
async def card(ctx, *, card_name : str):
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
            with open("./tmp.png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        await bot.delete_message(ctx.message)
        msg = await bot.send_file(ctx.message.channel , "./tmp.png")
        os.remove("./tmp.png")
        await asyncio.sleep(60)
        await bot.delete_message(msg)
    except FileNotFoundError:
        msg = await bot.send_message(ctx.message.channel, "Oups cette carte n'existe pas")
        await asyncio.sleep(3)
        await bot.delete_message(msg)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    if (limit > 9999):
        limit = 9999
    if (rolls > 50):
        rolls = 50
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

bot.run('MjMzOTYyMDkzODE1MTM2MjU2.Ct5nwA.HNZfuT67-jTc8CZqhyRT9F-5XN8')

