from discord.ext import commands
from discord import Intents
import os

intents = Intents.default()
intents.messages = True

bot = commands.Bot(
    command_prefix=os.environ["PEKOBOT_PREFIX"],
    intents=intents
)

bot.load_extension("extensions.pekofy")
bot.run(os.environ["PEKOBOT_TOKEN"])