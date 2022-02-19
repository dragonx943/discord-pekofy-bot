from discord.errors import HTTPException, Forbidden
from discord.ext import commands

import logging
import replies

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # specific events (mostly for logging)
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Succesfully logged in as {self.bot.user}!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        if isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(replies.handling.command_cooldown.format(round(error.retry_after, 2)))
        
        if isinstance(error, commands.CommandInvokeError):
            if isinstance(error.original, HTTPException) and error.original.code == 50035:
                # since Discord's API sends an HTTP exception itself,
                # there's a need for checking the error code.
                # code 50035 is the error code for "Invalid Form Body in content: Must be 2000 or fewer in length."
                return await ctx.send(replies.handling.message_too_long)
            
            if isinstance(error.original, Forbidden):
                return await ctx.send(replies.handling.cant_dm)
        
        logging.warning(f"A user tried to use {ctx.command} but got an error: {error}")
        await ctx.send(replies.handling.unexpected_error.format(error))

def setup(bot):
    bot.add_cog(Events(bot))