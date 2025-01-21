from telethon import TelegramClient, events, sync


api_id = '29541677' #api id
api_hash = 'd9643d40aeba2267782e67ef4fb11360' #api hash
bot_token = '7291435383:AAHdXjgA69ofF8JgO1gCQZYY5qjlL3n29ms' #Token bot

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# متنی قراره زیر پست ها اضافه شه
default_text = '@EvuIving'

@client.on(events.NewMessage)
async def handler(event):
    # آیدی عددی کانالتون
    if event.is_channel and event.chat_id == -1001634646053:
        
        new_message = event.message.message + default_text
        
        await client.edit_message(event.chat_id, event.message.id, new_message)

client.run_until_disconnected()
