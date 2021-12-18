from discord.ext import commands
from replies import emotions
import random

def random_chance(precent):
    return random.randint(1, 100) <= precent

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot:
            return

def setup(bot):
    bot.add_cog(Reactions(bot))