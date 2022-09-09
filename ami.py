from discord.ext import commands
import discord
import access


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    reaction = '👋'
    if message.author == client.user:
        return
    channel = client.get_channel(1017773583440814100)
    if message.content.startswith('$hello'):
        msg = await channel.send('Hello')
        await msg.add_reaction(reaction)

# @client.event
# async def send(message, channel):
#     if message.content.startswith("$send"):
#         channel = client.get_channel(int(channel))
#         await channel.send(f'I can send a message on {channel}')

# async def check_daily():
#     await 



client.run(access.token)
