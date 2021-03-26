from discord.ext import commands
import pekofy as peko # because i am gonna copy paste a lot of stuff
import credentials
import replies
import discord
import random

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

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
@commands.cooldown(1, 5, commands.BucketType.user) # one message every 5 seconds
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
@commands.cooldown(1, 5, commands.BucketType.user)
async def pekofy(ctx):
    if ctx.message.reference:
        reply = ctx.message.reference.resolved
    else:
        return
            
    if reply.author == bot.user:
        await ctx.send(replies.found_myself)
        return
    
    reply = reply.content
    reply = peko.pekofy(reply)
    
    if reply in ["NOTHING_CHANGED", "NO_LETTER"]:
        reply = random.choice(replies.nothing_changed_reply_list)
    
    await ctx.send(reply)
    
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pekopasta(ctx):
    await ctx.send(replies.cursed_pekopasta)
    
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def helpeko(ctx):
    await ctx.send(replies.helpeko)
    
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def credits(ctx):
    await ctx.send(replies.credits)
    
bot.run(credentials.token)