from typing import Dict, List
import dearpygui.dearpygui as dpg
from app import App
from gui.image import TelethonMessageImage
from .text import RGBText
from .base import BaseItem, NoDrawItem
from tkinter.filedialog import asksaveasfilename
import entities, re, webbrowser, os


class Content(BaseItem):

    def __init__(self, app: App, **kwargs):
        super().__init__(app, **kwargs)

        self.dialogs_messages: Dict[int, int] = {}
        self.message_items: List[Messageable] = []
        self.dialog: entities.Dialog
        self.contextItem: int = None

    def draw(self):

        with dpg.child_window(autosize_x=True, autosize_y=True, **self.dpg_args) as self.item:
            pass
        dpg.bind_item_theme(self.item, self.app.theme.contentTheme)

        with dpg.handler_registry():
            dpg.add_mouse_click_handler(callback = self.openContext, button = 1)

    def destroyContext(self):
        if self.contextItem: dpg.delete_item(self.contextItem)

    async def downloadFile(self, media: entities.Media):

        filename = media.generateFilename()
        path = asksaveasfilename(title="Скачать файл", initialfile=filename, defaultextension=media.mime_type)
        if path:
            await media.downloadFile(path)
        return path
        
    async def openFile(self, media: entities.Media):
        path = await self.downloadFile(media)
        if path:
            os.startfile(path)

    def downloadFileCallback(self, sender, appdata, media: entities.Media):
        self.app.createTask(self.downloadFile(media))
        self.destroyContext()

    def openFileCallback(self, sender, appdata, media: entities.Media):
        self.app.createTask(self.openFile(media))
        self.destroyContext()

    def copyMessageText(self, sender, appdata, userdata):
        dpg.set_clipboard_text(userdata)
        self.destroyContext()

    def openWeb(self, sender, appdata, userdata):
        webbrowser.open_new_tab(userdata)
        self.destroyContext()

    def openContext(self):

        for item in self.message_items:
            if dpg.is_item_hovered(item.item):
                with dpg.window(popup=True, pos=dpg.get_mouse_pos(local=False), no_move=True) as self.contextItem:
                    dpg.add_button(label = "Скопировать", callback = self.copyMessageText, user_data=item.message.message)
                    if item.message.media:
                        if item.message.media.webable:
                            dpg.add_button(label = "Открыть в браузере", callback = self.openWeb, user_data=item.message.media.web_url)
                        if item.message.media.downloadable:
                            dpg.add_button(label = "Скачать", callback = self.downloadFileCallback, user_data=item.message.media)
                            dpg.add_button(label = "Скачать и открыть", callback = self.openFileCallback, user_data=item.message.media)
                dpg.bind_item_theme(self.contextItem, self.app.theme.transparentButton)
                break

    def changeDialog(self, dialog: entities.Dialog):

        self.dialog = dialog
        self.dialogs_messages.setdefault(self.dialog.id, 50)
        self.app.createTask(self.loadMessages(), True)

    def loadMore(self):

        self.dialogs_messages[self.dialog.id] += 50
        self.app.createTask(self.loadMessages(), True)

    def resetDialog(self):

        del self.dialogs_messages[self.dialog.id]
        self.dialog.messages.clear()
        self.changeDialog(self.dialog)

    async def loadMessages(self):

        self.clearChildrens()
        self.message_items.clear()
        messages = await self.dialog.getChatMessages(self.dialogs_messages[self.dialog.id])

        btn = dpg.add_button(width=self.get_size()[0] - 15, label = "Обновить диалог", callback = self.resetDialog, parent = self.item)
        dpg.bind_item_theme(btn, self.app.theme.resetButton)

        btn = dpg.add_button(width=self.get_size()[0] - 15, label = "Загрузить больше", callback = self.loadMore, parent = self.item)
        dpg.bind_item_theme(btn, self.app.theme.loadButton)

        for message in messages:
            msg = Message(self.app, message, parent = self.item)
            self.message_items.append(msg)
            await msg.draw()

class Messageable(NoDrawItem):

    def __init__(self, app: App, message: entities.Message, **kwargs):
        super().__init__(app, **kwargs)

        self.message = message

    async def drawAttachments(self, already_forward: bool = False):

        self.image = None
        self.reply = None

        if self.message.media and self.message.media.is_photo and not isinstance(self, ReplyMessage): # ReplyMessages have a problem with images
            self.image = TelethonMessageImage(self.app, self.message.media)
            self.image.draw()
            self.app.createTask(self.image.downloadTexture(), callback = self.updateSize if isinstance(self, ReplyMessage) else None)

        if (self.message.reply_to or self.message.fwd_from) and not already_forward:
            self.reply = ReplyMessage(
                self.app, 
                await self.message.getReply() if self.message.reply_to else self.message
            )
            self.app.contentItem.message_items.append(self.reply)
            await self.reply.draw()

class Message(Messageable):

    async def draw(self):

        with dpg.group(**self.dpg_args) as self.item:

            colors = self.app.theme.colors
            author = await self.message.getUser()
            if self.message.media and not self.message.media.is_photo and not self.message.fwd_from:
                media = f"{colors.Media.value}[ {self.message.media.name} ]"
            else: media = ""

            RGBText(
                self.app, 
                f"{colors.Timestamp.value}{self.message.readableTimestamp}  {colors.Selection.value}{author.name}: {colors.Text.value}{self.message.message if not self.message.fwd_from else ''} {media}", 
                indent = 10, 
                wrap = 440
            ).item

            await self.drawAttachments()

class ReplyMessage(Messageable):

    def updateSize(self, res = None):
        
        if self.reply:
            self.text_width = max(self.text_width, self.reply.text_width) + 10
            self.text_height = self.text_height + self.reply.text_height
            dpg.configure_item(
                self.item, 
                width = self.text_width,
                height = self.text_height
            )

    async def draw(self):
    
        author = await (self.message.getForwardUser() if self.message.fwd_from else self.message.getUser())
        colors = self.app.theme.colors
        if self.message.media and not self.message.media.is_photo:
            media = f"{colors.Media.value}[ {self.message.media.name} ]"
        else: media = ""
        texts = [
            f"{'Переслано' if self.message.fwd_from else 'Сообщение'} от {colors.Selection.value}{author.name}  {colors.Timestamp.value}{self.message.readableTimestamp}",
            f"{colors.Text.value}{self.message.message} {media}"
        ]
        self.text_width = dpg.get_text_size(max(map(lambda t: re.sub("\{......}", "", t), texts), key=len))[0] + 10
        self.text_height = dpg.get_text_size(re.sub("\{......}", "", "\n".join(texts)))[1] + 20
        with dpg.child_window(width=self.text_width, height=self.text_height, indent=5, no_scrollbar=True, no_scroll_with_mouse=True, **self.dpg_args) as self.item:
            RGBText(self.app, texts[0], indent=5)
            RGBText(self.app, texts[1], indent=5)

            await self.drawAttachments(bool(self.message.fwd_from))
            self.updateSize()
        dpg.bind_item_theme(self.item, self.app.theme.replayTheme)