import json
import discord
from discord.ext import commands
from discord.webhook import RequestsWebhookAdapter
import requests
client = discord.Client()
command_pre = '$'




@client.event 
async def on_ready():
    print("bot is ready")


@client.event
async def on_message(message):
        
    if message.content.startswith(command_pre + 'help'):
            await message.channel.send("Hi, Welcome to Sids Valorant Bot! To use this bot, type $v 'valorant username' 'tagline'! :)")

    
        
           

        
    if message.content.startswith(command_pre + 'v'):
            stats = message.content.split(" ",2)
            username = (stats[1])
            tagline = (stats[2])
            req = requests.get('https://api.henrikdev.xyz/valorant/v1/mmr/na/' + username + '/' + tagline)
            data = (req.json())
            rank = (data['data']['currenttierpatched'])
            await message.channel.send('your rank is ' + rank)


   
            
            
        

            
          

      

            





 



     
    
    
   

client.run('OTA5ODY0MjAwMTA3NTg5Njc1.YZKfEQ.dBfuCV_nSph1Ce9uYx1sZVJAh9k')





   
    
