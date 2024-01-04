from typing import List, Dict
import telethon.tl.custom.dialog as dialog
import telethon.types
from entities.media import Media
from gui.image import TelethonMessageImage
import app as main
import io, tg, entities

class Dialog:

    def __init__(self, tg: "tg.TelegramService", tl_dialog: dialog.Dialog):

        self.tg = tg
        self.tl_dialog = tl_dialog
        self.id = self.entity.id
        self.name = self.entity.name
        self.photo = self.entity.photo
        self.last_message: telethon.types.Message = tl_dialog.message
        self.media: Dict[int, Media] = {}
        self.messages: List[entities.Message] = []

    async def getChatMessages(self, limit: int = 50, **kwargs) -> List[entities.Message]:

        left = limit - len(self.messages)
        if left > 0:
            max_id = self.messages[0].id if self.messages else 0
            messages = [entities.Message(self.tg, self, message) for message in await self.tg.client.get_messages(self.entity.id, limit = left, max_id = max_id, **kwargs)]
            self.messages = messages[::-1] + self.messages
        return self.messages[:limit]

    async def downloadMedia(self, media: "entities.Media") -> io.BytesIO:

        if media.id in self.media: return self.media[media.id]
        file = io.BytesIO()
        await media.downloadFile(file)
        self.media[media.id] = file
        return file

    async def downloadPhoto(self) -> io.BytesIO:

        file = io.BytesIO()
        await self.tg.client.download_profile_photo(self.entity.entity, file)
        return file

    @property
    def entity(self) -> entities.User | entities.Chat:

        entity = self.tl_dialog.entity
        if isinstance(entity, telethon.types.User): return entities.User(self.tg, entity)
        elif isinstance(entity, telethon.types.Chat): return entities.Chat(self.tg, entity)