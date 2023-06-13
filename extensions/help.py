from discord.ext import commands
from discord import Embed, ChannelType

from datetime import datetime
import replies

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["tasukeru"])
    async def helpeko(self, ctx):
        embed = Embed(
            title=replies.docs.title,
            description=replies.docs.description,
            colour=0xa5cdfb,

            timestamp=datetime.now(),
        )
        embed.set_footer(text=f"Invoked by {str(ctx.author)}", icon_url=str(ctx.author.avatar_url))

        for command in replies.docs.help.values():
            embed.add_field(
                name=command.get("usage"),
                value=command.get("description")
            )

        await ctx.author.send(embed=embed)

        if ctx.channel.type != ChannelType.private:
            await ctx.message.reply(replies.docs.dm_check, mention_author=False)

        #if datetime.now() < datetime(2022, 3, 12):
        #    # not sending the birthday embed after a week from March 5th
        #    await ctx.author.send(embed=self.birthday())
    
    def birthday(self):
        embed = Embed(
            title=replies.docs.birthday_title,
            description=replies.docs.birthday_description,
            colour=0xff9e3d
        )
        return embed
    
    @commands.command()
    async def credits(self, ctx):
        await ctx.message.reply(replies.docs.credits)
    
    @commands.command()
    async def invite(self, ctx):
        await ctx.message.reply(replies.docs.invite)
    
def setup(bot):
    bot.add_cog(Help(bot))