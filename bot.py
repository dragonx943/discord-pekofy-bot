import pekofy as peko # because i am gonna copy paste a lot of stuff
import credentials
import replies
import discord
import random

client = discord.Client()
keyphrase = '!pekofy'

def reply_chance(percent):
    return random.randint(0, 100) <= percent

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # pain peko (not used regex for faster results)
    if message.content.lower() in ["pain", "pain.", "pain...", "pain peko", "pain peko."] and reply_chance(50):
        await message.channel.send(replies.pain_peko_reply)

    # hey moona
    if "moona" in message.content.lower() and "pekora" in message.content.lower() and reply_chance(25):
        await message.channel.send(replies.hey_moona_reply)
    
    # pekofy command
    if keyphrase in message.content:
        channel = message.channel
        reply = await channel.history(limit=2).flatten()
        reply = reply[1].content

        reply = peko.pekofy(reply)
        # if it couldn't be pekofied, give a random pekora clip
        if reply in ["NOTHING_CHANGED", "NO_LETTER"]:
            reply = random.choice(replies.nothing_changed_reply_list)
        
        await message.channel.send(reply)

    if message.content == "!pekopasta":  # easter egg
        await message.channel.send(replies.cursed_pekopasta)
        
client.run(credentials.token)