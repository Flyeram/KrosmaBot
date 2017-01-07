import discord
from discord.ext import commands
import asyncio


def checkMemberRole(member, roleToCheck):
	roles = member.server.roles
	for i in range(len(roles)):
		if (roles[i].name == roleToCheck):
			role = roles[i]
	if (role in member.roles):
		return True
	else:
		return False

def getChannelByName(bot, serverName, channelName):
	for server in bot.servers:
		if (server == serverName):
			currentServer = server
			break
	for chan in currentServer.channels:
		if (chan.name == channelName):
			return chan