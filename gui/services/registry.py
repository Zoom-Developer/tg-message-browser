import dearpygui.dearpygui as dpg
import app as main

big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
small_let_end = 0x00FF  # small "я" in cyrillic alphabet
remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped
chars_remap = {0x00A8: 0x0401, 0x00B8: 0x0451, 0x00AF: 0x0407, 0x00BF: 0x0457, 0x00B2: 0x0406, 0x00B3: 0x0456, 0x00AA: 0x0404, 0x00BA: 0x0454}

class RegistryService:

    def __init__(self, app: "main.App"):

        self.app = app

    def bindFont(self):

        dpg.bind_font(self.mainFont)

    def registerFonts(self):

        with dpg.font_registry():
            self.mainFont = self.addCyrilicFont(self.app.res.getPath("RobotoCondensed-Bold.ttf"), 20)
    
    def registerTextures(self):

        with dpg.texture_registry():
            self.userIcon = self.addImageTexture(self.app.res.getPath("user.png"))
            self.fileIcon = self.addImageTexture(self.app.res.getPath("file.png"))

    def addImageTexture(self, path: str) -> int:

        width, height, channels, data = dpg.load_image(path)
        return dpg.add_static_texture(width=width, height=height, default_value=data)

    def toCyrilic(self, text) -> str:

        out = []
        for i in range(0, len(text)):
            if ord(text[i]) in chars_remap:
                out.append(chr(chars_remap[ord(text[i])]))
            elif ord(text[i]) in range(big_let_start, small_let_end + 1):
                out.append(chr(ord(text[i]) + alph_shift))
            else:
                out.append(text[i])
        return ''.join(out)
    
    def addCyrilicFont(self, path, size):

        with dpg.font(file = path, size = size) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            biglet = remap_big_let
            for i1 in range(big_let_start, big_let_end + 1):
                dpg.add_char_remap(i1, biglet)
                dpg.add_char_remap(i1 + alph_len, biglet + alph_len)
                biglet += 1
            for char in chars_remap.keys():
                dpg.add_char_remap(char, chars_remap[char])

        return font