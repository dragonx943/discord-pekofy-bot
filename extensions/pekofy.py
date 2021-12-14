from discord.ext import commands
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
            await ctx.send(embed=await pekofication.pekofy_embed(message.embeds[-1]))
        else:
            await ctx.send(await pekofication.pekofy(message.clean_content))

def setup(bot):
    bot.add_cog(Pekofy(bot))