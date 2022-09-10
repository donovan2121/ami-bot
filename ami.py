from time import timezone
from webbrowser import get
from discord.ext import commands, tasks
import discord
# import access
from datetime import datetime, time, timedelta
import asyncio
import os



intents = discord.Intents.default()
bot = commands.Bot("$", intents=intents)
intents.message_content = True
target = time(8, 0 , 0)



client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(target)
    await task_scheduler()
    # task_scheduler.start()



@client.event
async def send_checkin(message):
    reactions = ['😃', '🤓', '😖', '😨', '😡']
    
    channel = client.get_channel(1017773583440814100)
    print(channel)
    msg = await channel.send('How are you feeling today?')

    for reaction in reactions:
        await msg.add_reaction(reaction)

def get_time_seconds(param_target):
    current_time = datetime.now()
    if param_target == time(1, 0, 0):
        # tomorrow = datetime.combine(current_time.date() + timedelta(days=1), param_target)
        tomorrow = datetime.combine(current_time.date() + timedelta(days=1), param_target)
        seconds = (tomorrow - current_time).total_seconds()  
    else:
        # time_target = datetime.combine(current_time.date() + timedelta(days=1), param_target)
        time_target = datetime.combine(current_time.date() + timedelta(days=1), param_target)
        seconds = (time_target - current_time).total_seconds()   

    print(seconds)
    return seconds

# @tasks.loop(minutes=5)
async def task_scheduler():
    current_time = datetime.now()
    message = 'How are you feeling today?'


    if current_time.time() > target:  
        await asyncio.sleep(get_time_seconds(time(1, 0, 0)))  

    while True:
        await asyncio.sleep(get_time_seconds(target))
        await send_checkin(message)
        await asyncio.sleep(get_time_seconds(time(1, 0, 0)))



class MyBot(commands.Bot):
    async def setup_hook(self):
        self.loop.create_task(task_scheduler())


if __name__ == "__main__":
    bot = MyBot("$", intents=intents)
    client.run(os.environ('AMI_TOKEN'))

