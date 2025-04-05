import requests
import asyncio
import urllib.parse
from nexichat import nexichat as app
from pyrogram import Client, filters, enums

def ask_query(query: str) -> str:
    try:
        url = f"https://chatwithai.codesearchdev.workers.dev/?chat={urllib.parse.quote(query)}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get("data", "Aaru couldn't find an answer 😔.")

    except Exception as e:
        return f"❖ eva got an error: {str(e)}. Contact @moviiieeeesss."

    return "❖ eva encountered an unknown issue. Contact @moviiieeeesss."

async def send_typing_action(client: Client, chat_id: int, duration: int = 2):
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)

@app.on_message(filters.command("ask"))
async def handle_query(client: Client, message):
    if len(message.command) < 2:
        await message.reply_text("💡 Ask eva anything, I'm here to help.")
        return

    user_query = message.text.split(" ", 1)[1]

    await send_typing_action(client, message.chat.id)
    response = ask_query(user_query)

    await message.reply_text(response)
