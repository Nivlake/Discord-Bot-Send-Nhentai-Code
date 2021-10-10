#Library
import discord
from Server import keep_alive
from random import randint
from random import choice
import time
import sys
import os
import random

#Variabel
client = discord.Client()
#Function
def randomhen2():
  num=random.randint(1,300000)
  hentai_pick="https://nhentai.net/g/{}/".format(num)
  return(hentai_pick)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Discord Client Event
@client.event
async def on_ready():
  delay_print('{0.user} Telah logged in, Ready For Run'.format(client))
  change_status.start()


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    elif message.content.startswith("!hentai"):
      nhentai=randomhen2()
      await message.channel.send(nhentai)
    
#SERVER
keep_alive()
client.run(os.getenv('TOKEN'))