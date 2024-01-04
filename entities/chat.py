import telethon.types
import tg

class Chat:

    def __init__(self, tg: "tg.TelegramService", tl_chat: telethon.types.Chat):

        self.tg = tg
        self.entity = tl_chat
        self.id = tl_chat.id
        self.name = tl_chat.title
        self.photo = tl_chat.photo