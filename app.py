import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from google import genai
from io import StringIO
# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set up Gemini
client1 = genai.Client(api_key=GEMINI_API_KEY)

# Intents & Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Synced {len(synced)} slash command(s)")
    except Exception as e:
        print("❌ Slash sync failed:", e)
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Optional: Add a prefix filter to only respond to messages that mention the bot or start with "bot"
    if bot.user.mentioned_in(message):
        try:
            thinking = await message.channel.send("💭 Thinking...")

            response = client1.models.generate_content(
                model="gemini-2.0-flash",
                contents=[{"role": "user", "parts": [{"text": message.content}]}]
            )

            # If response too long for Discord message
            if len(response.text) > 2000:
                file = discord.File(fp=StringIO(response.text), filename="response.md")
                await message.channel.send(file=file)
            else:
                await message.channel.send(f"{message.author.mention}{response.text}")

            await thinking.delete()

        except Exception as e:
            print("⚠️ Error in on_message:", e)
            await message.channel.send("❌ Something went wrong while talking to Gemini!")

    # Let commands still work
    await bot.process_commands(message)

# Custom /who-made-you command
@bot.tree.command(name="who_made_you", description="Find out who created this bot!")
async def who_made_you(interaction: discord.Interaction):
    await interaction.response.send_message("I am made by Aravind! 🧠✨")

bot.run(TOKEN)

