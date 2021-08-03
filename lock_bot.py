import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODcxOTE3OTg4NjM3NDYyNTQ4.YQiS5w.dRJ54g6dzmQY-dJcGuus984c2A0')
