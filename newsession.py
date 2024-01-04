from telethon.sync import TelegramClient
from config import *
import asyncio

async def main():

    client = TelegramClient(SESSION_NAME, API_ID, API_HASH, system_version="4.16.30-vxCUSTOM")
    phone = input("Номер телефона: ")
    password = input("Облачный пароль при наличии: ")
    await client.start(phone = phone, password = password)

asyncio.run(main())