from typing import Tuple, List
import app as main
import dearpygui.dearpygui as dpg

class BaseItem:

    item: int

    def __init__(self, app: "main.App", **kwargs):
        
        self.app = app
        self.dpg_args = kwargs
        self.draw()

    def get_pos(self) -> Tuple[int, int]:
        return dpg.get_item_pos(self.item)
    
    def get_size(self) -> List[int]:
        return dpg.get_item_rect_size(self.item)
    
    @property
    def childrens(self) -> List[int]:
        return dpg.get_item_children(self.item)
    
    def clearChildrens(self):
        dpg.delete_item(self.item, children_only = True)

    def draw(self):
        raise NotImplementedError
    
class NoDrawItem(BaseItem):

    def __init__(self, app: "main.App", **kwargs):

        self.app = app
        self.dpg_args = kwargs