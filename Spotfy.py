import discord
from Farsofsok import Outing

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content  != "":

        msg = Outing(message.content,Pname = message.author.name).Print

        await message.channel.send(msg)

client.run()#Token
