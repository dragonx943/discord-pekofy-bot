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

bot = commands.Bot(command_prefix=os.environ["PEKOBOT_PREFIX"], intents=intents)

# specific events (mostly for logging)
@bot.event
async def on_ready():
    logging.info(f"Succesfully logged in as {bot.user}!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    
    logging.warning(f"A user tried to use {ctx.command} but got an error: {error}")

# loading extensions
bot.load_extension("jishaku")
bot.load_extension("extensions.pekofy")
bot.load_extension("extensions.reactions")

bot.run(os.environ["PEKOBOT_TOKEN"])
logging.info("Shutting down...\n")