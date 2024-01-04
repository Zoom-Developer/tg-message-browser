from typing import Dict, List
from telethon import TelegramClient
import telethon.types as tl_types
from entities import Chat, Message, User, Dialog, Channel, UndefinedEntity


class TelegramService:

    def __init__(self, client: TelegramClient):

        self.client = client
        self.users: Dict[int, User] = {}
        self.dialogs: List[Dialog] = []

    async def getEntity(self, peer: tl_types.TypePeer) -> User | Channel:

        if isinstance(peer, tl_types.PeerChannel):
            user_id = peer.channel_id
            cls = Channel
        else:
            user_id = peer.user_id
            cls = User

        if user_id in self.users: return self.users[user_id]

        try: entity = cls(self, await self.client.get_entity(user_id))
        except: entity = UndefinedEntity()

        self.users[user_id] = entity
        return entity

    async def getDialogs(self) -> List[Dialog]:

        if not self.dialogs:
            self.dialogs = [
                Dialog(self, dialog) for dialog in await self.client.get_dialogs() 
                if isinstance(dialog.entity, tl_types.Chat) or isinstance(dialog.entity, tl_types.User)
            ]
        return self.dialogs
    
    async def getChatMessages(self, chat: Chat, limit: int = 50, **kwargs) -> List[Message]:

        return self.client.get_messages(chat, limit = limit, **kwargs)