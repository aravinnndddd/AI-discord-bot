

# 🤖 Helper-chan — Discord AI Chatbot

Helper-chan is an AI-powered Discord bot built using the Discord API and Google’s Gemini language model. It responds to both slash commands and normal messages, providing intelligent answers to your questions. Whether you're coding, curious, or just chatting, Helper-chan is here to help!

---

## ✨ Features

- 💬 Responds to messages that start with "bot" or mentions the bot.
- ❓ Slash command `/who_made_you` to show the creator.
- 🧠 Powered by Google Gemini AI (gemini-2.0-flash) for generating intelligent responses.
- 📄 Sends long replies as `.md` file attachments if the response is too long for Discord messages.
- 🛡️ Ignores its own messages to prevent reply loops.

---

## 🛠️ Setup & Installation

Follow these steps to get the bot running:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/helper-chan.git
cd helper-chan
```
2. Install the required Python packages:
```
pip install discord.py python-dotenv google-generativeai
```
3. Set up environment variables:

    Create a .env file in the project root directory with the following content:
```
    TOKEN=your_discord_bot_token
    GEMINI_API_KEY=your_google_gemini_api_key
```
4. Run the bot:
```
python bot.py
```
🧪 Usage

    Mention the bot or just message to trigger a response:

        Example: @yourbot what is Python?

        Example: bot explain machine learning.

    Use the slash command /who_made_you to find out who created the bot.


⚙️ Credits

    discord.py: For the bot framework and handling Discord interactions.

    Google Gemini: For powerful language model responses.

    python-dotenv: For managing environment variables securely.


---

This should provide a good overview of how to set up, use, and understand the bot. Let me know if you need further modifications!

