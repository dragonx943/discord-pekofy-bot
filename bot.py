from discord.ext import commands
from discord import Intents
import logging, os

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    
    handlers=[
        logging.FileHandler(filename="discord.log", encoding="utf-8"),
        logging.StreamHandler() # for printing stuff to the console
    ]
)

# set up intents
intents = Intents.default()
intents.messages = True

# initialize the bot with the prefix and intents
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

# load extensions
bot.load_extension("extensions.events")
bot.load_extension("extensions.pekofy")
bot.load_extension("extensions.reactions")
bot.load_extension("extensions.help")

# run the bot
bot.run(os.getenv("PEKOBOT_TOKEN"))