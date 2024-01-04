import telethon.types
import entities
import tg

class Channel:

    def __init__(self, tg: "tg.TelegramService", tl_channel: telethon.types.Channel):

        self.tg = tg
        self.entity = tl_channel
        self.id = tl_channel.id
        self.name = tl_channel.title