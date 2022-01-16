from discord.ext import commands
from discord import Intents
import logging, os

# setting up logging
logger = logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    
    filename="logs/pekolog.log", 
    encoding="utf-8"
)

# message content intent is required for reactions (replying to a message with a keyword)
intents = Intents.default()
intents.messages = True

prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

# loading extensions
bot.load_extension("jishaku")

bot.load_extension("extensions.events")
bot.load_extension("extensions.pekofy")
bot.load_extension("extensions.reactions")
bot.load_extension("extensions.help")

bot.run(os.environ["PEKOBOT_TOKEN"])
logging.info("Shutting down...\n")
