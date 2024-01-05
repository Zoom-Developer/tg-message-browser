import io
import dearpygui.dearpygui as dpg
from app import App
from gui.image import TelethonImage
from .base import BaseItem
import asyncio, tg

class Dialogs(BaseItem):

    def __init__(self, app: App, **kwargs):
        super().__init__(app, **kwargs)

        app.createTask(self.getDialogs())

    def draw(self):

        with dpg.child_window(width=300, autosize_y=True, **self.dpg_args) as self.item:
            dpg.add_child_window(height=5)
            self.dialogGroup = dpg.add_group()
        dpg.bind_item_theme(self.item, self.app.theme.usersTheme)

    async def getDialogs(self):

        dialogs = await self.app.tg.getDialogs()
        for dialog in dialogs:
            Dialog(self.app, dialog, parent = self.dialogGroup)

class Dialog(BaseItem):

    def __init__(self, app: App, dialog: tg.Dialog, **kwargs):
        self.dialog = dialog

        super().__init__(app, **kwargs)

    async def selectDialog(self, sender, appdata, dialog: tg.Dialog):
        await self.app.contentItem.changeDialog(dialog)

    def draw(self):

        with dpg.child_window(indent=10, width=270, height=70, no_scrollbar=True, no_scroll_with_mouse=True, **self.dpg_args) as self.item:
            with dpg.group(horizontal=True):
                img = TelethonImage(self.app, self.dialog, 70, 70)
                img.draw()
                self.app.createTask(img.downloadTexture())
                with dpg.group():
                    dpg.add_text(self.dialog.name)  
                    dpg.add_text(self.dialog.last_message.message)
                btn = dpg.add_button(width=280, height=70, pos=self.get_pos(), user_data=self.dialog, callback=self.selectDialog)
                dpg.bind_item_theme(btn, self.app.theme.transparentButton)
                
        dpg.bind_item_theme(self.item, self.app.theme.dialogTheme)