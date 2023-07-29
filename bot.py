import logging
import os

from discord import Intents
from discord.ext import commands

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    
    handlers=[
        logging.FileHandler(filename="discord.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# initialize intents
intents = Intents.default()

# enable the required intents
intents.message_content = True

# initialize the bot with the prefix and intents
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

# load extensions
bot.load_extension("extensions.events")
bot.load_extension("extensions.pekofy")
bot.load_extension("extensions.reactions")
bot.load_extension("extensions.help")

# run the bot
bot.run(os.getenv("DISCORD_TOKEN"))