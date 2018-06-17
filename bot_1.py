import discord

client = discord.Client()


@client.event
async def on_ready():
    print("{0} has logged in.".format(client.user))


@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        await client.send_message(message.channel, "PONG")


client.run("NDU2NjY0MTU0ODg3OTQ2MjUx.DgN24A.JAaBWjlXEKfL42ttE7c1TMA1xcc")
