import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!midjourney'):
        # запрос к ИИ Midjourney
        response = "Ответ от ИИ Midjourney"
        await message.channel.send(response)

client.run('MTA4ODk2OTcwODgxODE0OTQyNg.Gcu-tI.3MQ3PHZKWIv_480oBc8Aqky17noTRfFo46VT_g')