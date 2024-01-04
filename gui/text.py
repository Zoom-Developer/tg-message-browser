import dearpygui.dearpygui as dpg
from .base import BaseItem
import re, app as main


class Text(BaseItem):

    def __init__(self, app: "main.App", text: str = "", wrap: int = -1, **kwargs):
        self.text = text
        self.wrap = wrap

        super().__init__(app, **kwargs)

    def draw(self):

        self.item = dpg.add_text(self.text, **self.dpg_args)

class RGBText(Text):

    def draw(self):
        
        colors = re.findall("{(......)}", self.text)
        with dpg.group(horizontal=True, horizontal_spacing=0, **self.dpg_args) as self.item:
            for i, sub in enumerate(re.split("{......}", self.text), -1):
                if i > -1:
                    r, g, b = bytes.fromhex(colors[i])
                    dpg.add_text(sub, color=(r, g, b, 255), wrap = self.wrap)
                elif sub: dpg.add_text(sub, wrap = self.wrap)
