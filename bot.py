from discord.ext import commands
import discord

#import logging
import random

import pekofy as peko # because i am gonna copy paste a lot of stuff
import credentials
import replies

"""
# logger stuff
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""

prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_command=None)

def reply_chance(percent):
    return random.randint(0, 100) <= percent

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(
        activity = discord.Activity(
            type = discord.ActivityType.playing,
            name = replies.status_content
        )
    )

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:
        return

    # pain peko (not used regex for faster results)
    if message.content.lower() in ["pain", "pain.", "pain...", "pain peko", "pain peko."] and reply_chance(50):
        await message.channel.send(replies.pain_peko_reply)

    # hey moona
    if "moona" in message.content.lower() and "pekora" in message.content.lower() and reply_chance(25):
        await message.channel.send(replies.hey_moona_reply)

    # insulting people
    if message.content.lower() == "insult me peko":
        await message.channel.send(random.choice(replies.insults))

    # rating reactions
    if message.reference: # if the message is a reply
        if message.reference.resolved.author == bot.user: # if the reply is from pekofy bot
            if "good bot" in message.content.lower():
                await message.channel.send(random.choice(replies.thanks))
            if "bad bot" in message.content.lower():
                await message.channel.send(random.choice(replies.sorrys))         
            if "cute bot" in message.content.lower():
                await message.channel.send(random.choice(replies.cutes))
            if message.content.lower() in ["i love you", "love you", "love", "i love you peko", "love you peko", "love peko"]:
                await message.channel.send(random.choice(replies.loves))

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.guild) # 5s server cooldown
async def pekofy(ctx):
    if ctx.message.reference: # if a message does have a reply
        reply = ctx.message.reference.resolved
    else:
        await ctx.send(replies.no_reply)
        return
            
    if reply.author == bot.user:
        await ctx.send(replies.found_myself)
        return
    
    content = reply.content

    # if a reply does have any embeds
    if reply.embeds:
        reply = peko.embed_pekofy(reply.embeds[0])
    elif reply.mentions:
        for member in reply.mentions:
            content = content.replace(member.mention.replace("<@", "<@!"), f"\@{member.name}")
            content = content.replace(member.mention, f"\@{member.name}")

        reply = peko.pekofy(content)
    else:
        reply = peko.pekofy(content)
    
    if reply in ["NOTHING_CHANGED", "NO_LETTER"]:
        reply = random.choice(replies.nothing_changed_reply_list)
    
    # if reply is an embed
    if isinstance(reply, discord.Embed):
        await ctx.send(embed = reply)
    else:
        await ctx.send(reply)
    
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.guild) # 10s server cooldown
async def pekopasta(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send(replies.cursed_pekopasta)
    else:
        await ctx.send(replies.cursed_pekopasta_censored)

### info commands   
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user) # 5s user cooldown
async def helpeko(ctx):
    await ctx.send(embed=replies.helpeko)
    
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user) # 5s user cooldown
async def credits(ctx):
    await ctx.send(replies.credits)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user) # 5s user cooldown
async def invite(ctx):
    await ctx.send(replies.invite)

### owner only commands
@bot.command()
@commands.is_owner()
async def pekodebug(ctx):
    content = replies.pekodebug_template.format(
        len(bot.guilds),
        round(bot.latency * 1000)
    )
    await ctx.send(content)

### cooldown handling
@pekofy.error
@pekopasta.error
async def cooldown_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(replies.cooldown_msg.format(
            round(error.retry_after, 2)
        ))

bot.run(credentials.token)