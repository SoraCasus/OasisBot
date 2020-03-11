import discord

from get_memes import get_memes
from profanity_check import predict, predict_prob

bot = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    text = message.content

    res = predict([text])

    if 1 in res:
        await message.channel.send('Goodness me, language!')

    if 'cuck' in text.lower():
        await message.channel.send('Goodness me, I don\'t know what this... cuck word means but you make it sound like something profane')

    if text.startswith('$late'):
        await message.channel.send('Ben, my dear, it appears you\'re late again. I know you can do better dear...')

    if text.startswith('$smite'):
        await message.channel.send('*Smites {}*'.format(text.split()[1]))

    if 'bot' in text.lower():
        await message.channel.send('I\'m sorry dear, I believe **you\'re** the "bot" here')

    if 'heck' in text.lower():
        await message.channel.send('{}, you\'re on thin **fucking** ice'.format(message.author.mention))

    if 'paper' in text.lower():
        await message.channel.send("Fredrick, why?")

    if '69' in text.lower():
        await message.channel.send('Nice')

    if '420' in text.lower():
        await message.channel.send('Ayy lmao')

    if '69420' in text.lower():
        await message.channel.send('The god number!')

    if message.author.name == 'SampleTex':
        await message.channel.send('Why would you mount a frisbee to your wall')

    if text.startswith('$meme'):
        # Scrape meme from reddit
        get_memes()
        # Send the meme
        await message.channel.send("", file=discord.File('meme.png'))

    if 'roll' in text.lower():
        await message.channel.send("", file=discord.File('song.mp3'))

    if 'smite' in text.lower():
        await message.channel.send("", file=discord.File('smite.png'))

    if 'honk' in text.lower():
        await message.channel.send("**HONK**", file=discord.File('HONK.png'))


cred = open("cred.dat", "r")

bot.run(cred.read())