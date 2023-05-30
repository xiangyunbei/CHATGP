import discord
from discord.ext import commands
import aiohttp

TOKEN = 'Bot-Token'
API_KEY = 'Key'

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
        print ("Bot has Connected to Discord!")

@bot.command()
async def gpt(ctx: commands.Context, *, prompt: str):
        async with aiohttp.ClientSession() as session:
                payload = {
                        "model": "text-davinci-003",
                        "prompt": prompt,
                        "temperature": 0.5,
                        "max_tokens": 200,
                        "presence_penalty": 0,
                        "frequency_penalty": 0,
                        "best_of": 1,
                }
                
                headers = {"Authorization": f"Bearer {API_KEY}"}
                async with session.post ("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
                        response = await resp.json()
                        embed = discord.Embed(title="Chat GPT's Response:", description=response["choices"][0]["text"])
                        await ctx.reply(embed=embed)


bot.run(TOKEN)
[app]  
requires = ["discord.py-rpc>=1.2.2"]
