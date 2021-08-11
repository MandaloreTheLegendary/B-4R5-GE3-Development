import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ch.in'):
        login_user = message.author
        await message.channel.send(login_user + ' has logged in.')

#Need to create a .env file and environment variable for token for security
client.run('ODcxOTE3OTg4NjM3NDYyNTQ4.YQiS5w.dRJ54g6dzmQY-dJcGuus984c2A0')
