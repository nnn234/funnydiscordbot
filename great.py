from googleapiclient.discovery import build
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('ready')

import random

@client.command(aliases=['search'])
async def _search(ctx, *, query):
        service = build("customsearch", "v1",developerKey='AIzaSyC6CcdMjjHnyMH80RW7PAXTrFOXwyfwFjI')
        res = service.cse().list(
                q=query,
                filter="1", # filter duplicates
                start=1,
                cx='43e2d90ea5d6a1a82',
                searchType='image'
            ).execute()
        print(res)
        if (res.get('items') == None):
                await ctx.send("Error: something stupid happened; try again")
        #links = [x['link'] for x in res['items']]
        #await ctx.send(random.choice(links))
        for x in res['items']:
                await ctx.send(x['link'])

client.run('ODMxNzI0OTE4ODIzMDU5NDU5.YHZaMQ.-qXQ8YZguI63r6FffivtvDbCEIg')
