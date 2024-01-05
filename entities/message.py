import telethon.types
import entities
import tg

class Message:

    def __init__(self, tg: "tg.TelegramService", dialog: "entities.Dialog", tl_message: telethon.types.Message):

        self.tg = tg
        self.entity = tl_message
        self.dialog = dialog
        self.id = tl_message.id
        self.author = tl_message.from_id
        self.message = tl_message.message
        self.timestamp = tl_message.date
        self.reply_to = tl_message.reply_to.reply_to_msg_id if tl_message.reply_to else None
        self.fwd_from = tl_message.fwd_from.from_id if tl_message.fwd_from else None
        self.media = entities.Media(tg, self, tl_message.media) if tl_message.media else None

    @property
    def readableTimestamp(self) -> str:
        return self.timestamp.astimezone().strftime('%d.%m.%Y %H:%M:%S')

    async def getReply(self) -> "Message":
        entity = await self.tg.client.get_messages(self.dialog, ids=self.reply_to)
        if not entity: return entities.UndefinedMessage()
        return Message(self.tg, self.dialog, entity)

    async def getForwardUser(self) -> "entities.User":
        return await self.tg.getEntity(self.fwd_from)

    async def getUser(self) -> "entities.User":

        if not self.author: return self.dialog.entity
        return await self.tg.getEntity(self.author)