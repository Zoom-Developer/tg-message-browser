import sys, os

class ResourceService:

    def getPath(self, relative_path):

        try: base_path = sys._MEIPASS
        except Exception: base_path = os.path.abspath(".")
        return os.path.join(base_path, "gui/resources/" + relative_path)