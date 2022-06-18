from discord.ext import commands
from discord import Embed, ChannelType
import random

from modules import pekofication
import replies

def random_chance(precent):
    return random.randint(1, 100) <= precent

class Pekofy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    async def pekofy(self, ctx):
        if not ctx.message.reference: # reference is a reply to a message
            return await ctx.send(random.choice(replies.handling.no_reference))

        message = ctx.message.reference.resolved
        
        if message.embeds:
            response = await pekofication.pekofy_embed(message.embeds[-1])
        else:
            response = await pekofication.pekofy(message.clean_content)

        if response == "TOO_MANY_PEKOS":
            return await ctx.send(replies.handling.limit_reached)
        
        if response == message.clean_content:
            return await ctx.send(random.choice(replies.handling.no_change))
        
        if isinstance(response, Embed):
            await ctx.send(embed=response)
        else:
            await ctx.send(response)

    @commands.command()
    @commands.cooldown(1, 10.0, commands.BucketType.guild)
    async def pekopasta(self, ctx):     
        if ctx.channel.type == ChannelType.private or ctx.channel.is_nsfw():
            await ctx.send(replies.copypasta.nsfw)
        else:
            await ctx.send(replies.copypasta.sfw)
    
    @commands.command()
    @commands.cooldown(1, 10.0, commands.BucketType.guild)
    async def pekogacha(self, ctx):
        if random_chance(25):
            await ctx.message.reply(random.choice(replies.handling.gacha_win))
        else:
            await ctx.message.reply(random.choice(replies.handling.gacha_lose))

def setup(bot):
    bot.add_cog(Pekofy(bot))