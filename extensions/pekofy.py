from discord.ext import commands
from discord import Embed
import regex

from modules import pekofication
import replies

class Pekofy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pekofy')
    async def pekofy(self, ctx):
        if ctx.message.reference: # reference is a reply to a message
            message = ctx.message.reference.resolved
        else:
            return await ctx.send(replies.no_reference)

        if message.embeds:
            response = await pekofication.pekofy_embed(message.embeds[-1])
        else:
            response = await pekofication.pekofy(message.clean_content)

        if response == message.clean_content:
            return await ctx.send(replies.no_change)

        if isinstance(response, Embed):
            await ctx.send(embed=response)
        else:
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Pekofy(bot))