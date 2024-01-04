import dearpygui.dearpygui as dpg
from .base import NoDrawItem
from PIL import Image as img
from telethon.types import UserProfilePhotoEmpty, ChatPhotoEmpty
import requests, numpy, io, array, app as main, entities


class Image(NoDrawItem):

    def __init__(self, app: "main.App", texture: int, width: int = 0, height: int = 0, **kwargs):
        self.texture = texture
        self.img_width = width
        self.img_height = height

        super().__init__(app, **kwargs)

    def draw(self):
        
        self.item = dpg.add_image(width = self.img_width, height = self.img_height, texture_tag = self.texture, **self.dpg_args)

    def updateTexture(self, texture: int):

        self.texture = texture
        dpg.configure_item(self.item, texture_tag = texture, width = self.img_width, height = self.img_height)

class BytesImage(Image):

    def __init__(self, app: "main.App", file: io.BytesIO, width: int = 0, height: int = 0, **kwargs):
        super().__init__(app, self.createTexture(file), width, height, **kwargs)

    def createTexture(self, file: io.BytesIO, update_sizes: bool = False) -> int:

        image = img.open(file)
        if self.img_width: 
            image = image.resize((self.img_width, self.img_height))
        if update_sizes:
            self.img_width, self.img_height = image.width, image.height
        image_arr = array.array("f", numpy.array(image).ravel() / 255)
        
        with dpg.texture_registry():
            return dpg.add_raw_texture(width=image.width, height=image.height, default_value=image_arr, format=dpg.mvFormat_Float_rgb)

class ExternalImage(BytesImage):

    def __init__(self, app: "main.App", url: str, width: int = 0, height: int = 0, **kwargs):

        super().__init__(app, self.downloadTexture(url), width, height, **kwargs)

    def downloadTexture(self, url: str) -> io.BytesIO:

        content = requests.get(url).content
        file = io.BytesIO(content)
        return file

class TelethonImage(BytesImage):

    def __init__(self, app: "main.App", dialog: "entities.Dialog", width: int = 0, height: int = 0, **kwargs):

        Image.__init__(self, app, app.registry.userIcon, width, height, **kwargs)
        self.dialog = dialog

    async def downloadTexture(self):

        if isinstance(self.dialog.photo, (ChatPhotoEmpty, UserProfilePhotoEmpty)) or not self.dialog.photo: return
        file = await self.dialog.downloadPhoto()
        texture = self.createTexture(file)
        self.updateTexture(texture)

class TelethonMessageImage(BytesImage):

    def __init__(self, app: "main.App", media: "entities.Media", width: int = 0, height: int = 0, **kwargs):

        Image.__init__(self, app, app.registry.fileIcon, width, height, **kwargs)
        self.media = media

    async def downloadTexture(self):

        file = await self.media.download()
        texture = self.createTexture(file)
        self.updateTexture(texture)