from datetime import datetime
import entities

class UndefinedEntity:

    def __init__(self):
        
        self.name = "Неизвестный пользователь"
        self.entity = None

class UndefinedMessage:

    def __init__(self):

        self.dialog = UndefinedEntity()
        self.id = None
        self.author = None
        self.message = "Неизвестное сообщение"
        self.timestamp = datetime.fromtimestamp(0)
        self.reply_to = None
        self.fwd_from = None
        self.media = None

    @property
    def readableTimestamp(self) -> str:
         return self.timestamp.strftime('%d.%m.%Y %H:%M:%S')

    async def getUser(self) -> "entities.User":
        return UndefinedEntity()