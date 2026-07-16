import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def about(ctx):
    await ctx.send("Poach v1.0 \n poach.enesyali.site \n All Rights Reserved")

@bot.event
async def on_message(message):
    


bot.run("YOUR_BOT_TOKEN")