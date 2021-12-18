from discord.ext import commands
from discord import Intents
import logging, os

# message content intent is required for reactions (replying to a message with a keyword)
intents = Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix=os.environ["PEKOBOT_PREFIX"], intents=intents)

# loading extensions
bot.load_extension("extensions.pekofy")
bot.load_extension("extensions.reactions")

bot.run(os.environ["PEKOBOT_TOKEN"])