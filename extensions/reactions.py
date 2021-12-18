from discord.ext import commands
import replies
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

        content = message.clean_content.lower()
        
        if any(x in content for x in replies.triggers.pain):
            if random_chance(25):
                return await message.channel.send(replies.handling.pain_peko)
            
        if all(x in content for x in replies.triggers.moona):
            if random_chance(25):
                return await message.channel.send(replies.handling.hey_moona)

        if content == replies.handling.insult_me_peko:
            return await message.channel.send(random.choice(replies.handling.insult_me_peko))
        
        if not message.reference:
            return
        
        if message.reference.resolved.author == self.bot.user:
            if any(x in content for x in replies.triggers.cute):
                return await message.channel.send(random.choice(replies.emotions.cute))

            if any(x in content for x in replies.triggers.love):
                return await message.channel.send(random.choice(replies.emotions.love))
            
            if any(x in content for x in replies.triggers.sorry):
                return await message.channel.send(random.choice(replies.emotions.sorry))

            if any(x in content for x in replies.triggers.thank):
                return await message.channel.send(random.choice(replies.emotions.thank))

def setup(bot):
    bot.add_cog(Reactions(bot))