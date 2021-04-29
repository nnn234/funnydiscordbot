from googleapiclient.discovery import build
import discord
from discord.ext import commands

import os
googlekey = os.eviron['SEARCH_KEY']
cx = os.eviron['CX']
discordkey = os.eviron['DISCORD_KEY']

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('ready')

import random

@client.command(aliases=['search'])
async def _search(ctx, *, query):
        service = build("customsearch", "v1",developerKey=googlekey)
        res = service.cse().list(
                q=query,
                filter="1", # filter duplicates
                start=1,
                cx=cx,
                searchType='image'
            ).execute()
        print(res)
        if (res.get('items') == None):
                await ctx.send("Error: something stupid happened; try again")
        #links = [x['link'] for x in res['items']]
        #await ctx.send(random.choice(links))
        for x in res['items']:
                await ctx.send(x['link'])

client.run(discordkey)
