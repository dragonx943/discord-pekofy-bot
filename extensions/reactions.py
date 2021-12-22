from discord.ext import commands, tasks
import replies
import random

def random_chance(precent):
    return random.randint(1, 100) <= precent

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        content = message.clean_content.lower()
        
        if any(x in content for x in replies.triggers.pain):
            if random_chance(25):
                return await message.channel.send(replies.handling.pain_peko)
            
        if all(x in content for x in replies.triggers.moona):
            if random_chance(25):
                return await message.channel.send(replies.handling.hey_moona)

        if content == replies.handling.insult_me_peko:
            return await message.channel.send(random.choice(replies.emotions.insult))
        
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

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.change_status.start()
    
    @tasks.loop(minutes=10.0)
    async def change_status(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=random.choice(replies.statuses.statuses))

def setup(bot):
    bot.add_cog(Reactions(bot))
    bot.add_cog(Status(bot))