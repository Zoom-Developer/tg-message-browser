import telethon.types
from telethon.hints import FileLike
import tg, io, entities

class Media:

    def __init__(self, tg: "tg.TelegramService", message: "entities.Message", media: "telethon.types.TypeMessageMedia"):

        self.tg = tg
        self.entity = media
        self.is_photo = isinstance(media, telethon.types.MessageMediaPhoto)
        self.message = message

    def generateFilename(self) -> str:
        return f"{self.message.dialog.id}_{self.id}.{self.filetype}"

    @property
    def filetype(self) -> str:
        return self.mime_type.split("/")[-1]

    @property
    def mime_type(self) -> str:
        if isinstance(self.entity, telethon.types.MessageMediaDocument):
            return self.entity.document.mime_type
        elif isinstance(self.entity, telethon.types.MessageMediaPhoto):
            return "image/png"

    @property
    def webable(self) -> bool:
        return isinstance(self.entity, telethon.types.MessageMediaWebPage)

    @property
    def web_url(self) -> str:
        return self.entity.webpage.url

    @property
    def downloadable(self) -> bool:
        return isinstance(self.entity, (telethon.types.MessageMediaPhoto, telethon.types.MessageMediaDocument))

    @property
    def id(self) -> int:
        if isinstance(self.entity, telethon.types.MessageMediaDocument):
            return self.entity.document.id
        elif isinstance(self.entity, telethon.types.MessageMediaPhoto):
            return self.entity.photo.id

    async def download(self) -> io.BytesIO:
        return await self.message.dialog.downloadMedia(self)
    
    async def downloadFile(self, file: FileLike):
        await self.tg.client.download_media(self.message.entity, file)

    @property
    def name(self) -> str:
        names = {
            telethon.types.MessageMediaPhoto: "Фотография",
            telethon.types.MessageMediaGeo: "Гео-позиция",
            telethon.types.MessageMediaContact: "Контакт",
            telethon.types.MessageMediaDocument: "Документ",
            telethon.types.MessageMediaWebPage: "Веб-страница",
            telethon.types.MessageMediaGame: "Игра",
            telethon.types.MessageMediaGeoLive: "Гео-позиция в реальном времени",
            telethon.types.MessageMediaPoll: "Голосование",
            telethon.types.MessageMediaDice: "Кости",
            telethon.types.MessageMediaStory: "История",
            telethon.types.MessageMediaGiveaway: "Раздача",
        }
        return names.get(type(self.entity), "Неизвестное медиа")