import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
  print("Logged in as")
  print(bot.user.name)
  print(bot.user.id)
  
bot.run(os.environ['BOT_TOKEN'])
