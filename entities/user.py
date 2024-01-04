import telethon.types
import tg

class User:

    def __init__(self, tg: "tg.TelegramService", tl_user: telethon.types.User):

        self.tg = tg
        self.entity = tl_user
        self.id = tl_user.id
        self.username = tl_user.username
        self.first_name = tl_user.first_name
        self.last_name = tl_user.last_name
        self.name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        self.photo = tl_user.photo