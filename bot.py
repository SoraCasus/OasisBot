import discord
import json
import sys

from get_memes import get_memes
from profanity_check import predict, predict_prob
from random import randrange

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

    if 'cuck' in text.lower():
        await message.channel.send('Goodness me, I don\'t know what this... cuck word means but you make it sound like something profane')

    if text.startswith('$late'):
        await message.channel.send('Ben, my dear, it appears you\'re late again. I know you can do better dear...')

    if text.startswith('$smite'):
        if len(text.split()) > 1:
            await message.channel.send('*Smites {}*'.format(text.split()[1]))
        else:
            await message.channel.send('I\'m not sure who to smite here dear...')

    if text.startswith('$oasis_on'):
        await message.channel.send("Oh, hello there dear")
        data = {}
        data['active'] = True

        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Psychiatric help 5¢"))

    if text.startswith('$oasis_off'):
        await message.channel.send("Oh... I'll see myself out then...")
        data = {}
        data['active'] = False

        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

        await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Crying in a corner"))

    if text.startswith('$meme'):
        # Scrape meme from reddit
        get_memes()
        # Send the meme
        await message.channel.send("", file=discord.File('meme.png'))

    active = False
    with open('settings.json') as jsonFile:
        data = json.load(jsonFile)
        if bool(data['active']) == True:
            active = True

    if not active:
        return

    if 1 in res:
        await message.channel.send('Goodness me, language!')

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

    if '666' in text.lower():
        await message.channel.send("Shhhh, don't say that too loud.... he might hear you!")

    if '12' in text.lower():
        await message.channel.send("Ah yes, my blessed number!")


    if message.author.name == 'SampleTex':
        if randrange(10) == 1:
            await message.channel.send('Why would you mount a frisbee to your wall?')

    if 'roll' in text.lower():
        await message.channel.send("", file=discord.File('song.mp3'))

    if 'smite' in text.lower():
        await message.channel.send("", file=discord.File('smite.png'))

    if 'honk' in text.lower():
        await message.channel.send("**HONK**", file=discord.File('HONK.png'))


cred = open("cred.dat", "r")

bot.run(cred.read())
