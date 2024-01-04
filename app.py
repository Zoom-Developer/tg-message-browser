from typing import Callable, Coroutine, Dict
from telethon import TelegramClient
from config import *
import dearpygui.dearpygui as dpg
import asyncio, gui, gui.services, tg, inspect, functools


class App:

    def __init__(self, client: TelegramClient, loop: asyncio.AbstractEventLoop):

        self.tg = tg.TelegramService(client = client)
        self.loop = loop
        self.registry = gui.services.RegistryService(self)
        self.res = gui.services.ResourceService()
        self.theme = gui.services.ThemeService()

        self.tasks: Dict[Coroutine | PriorityCoroutine, Callable | None] = {}
        self.bg_tasks: Dict[asyncio.Task, Callable | None] = {}

    def setup(self):

        dpg.create_context()
        dpg.create_viewport(
            title = "Tg Message Browser",
            width = 1000,
            height = 600,
            small_icon = self.res.getPath("icon.png"),
            large_icon = self.res.getPath("icon.png")
        )
        dpg.setup_dearpygui()

        self.registry.registerFonts()
        self.registry.registerTextures()
        self.registry.bindFont()
        self.theme.setupThemes()
        self.theme.bindTheme()

    async def start(self):

        dpg.set_primary_window(self.window, True)
        dpg.show_viewport()
        dpg.configure_app(manual_callback_management=True)
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
            jobs = dpg.get_callback_queue()
            await self._processTasks()
            await self._processCallbacks(jobs)
            await asyncio.sleep(0.01)
        dpg.destroy_context()

    def draw(self):

        with dpg.window() as self.window:
            with dpg.group(horizontal=True):
                self.dialogsItem = gui.Dialogs(self)
                self.contentItem = gui.Content(self)

    def _onBgTaskFinished(self, res: asyncio.Future, task: asyncio.Task, callback: Callable | None):

        if res.done():
            if callback:
                callback(res.result())
        else: res.exception()
        del self.bg_tasks[task]

    def _createBgTask(self, f: Coroutine, callback: Callable = None):

        bg_task = asyncio.create_task(f)
        self.bg_tasks[bg_task] = callback
        bg_task.add_done_callback(functools.partial(self._onBgTaskFinished, task = bg_task, callback = callback))

    def createTask(self, f: Coroutine, priority: bool = False, callback: Callable = None):

        if priority: f = PriorityCoroutine(f)
        self.tasks[f] = callback

    async def _processTasks(self):

        for task, callback in list(self.tasks.items()):
            priority = isinstance(task, PriorityCoroutine)
            if len(self.bg_tasks) >= 5 and not priority: break
            del self.tasks[task]
            self._createBgTask(task.coroutine if priority else task, callback)

    async def _processCallbacks(self, jobs):
        if jobs is None:
            pass
        else:
            for job in jobs:
                if job[0] is None:
                    continue
                sig = inspect.signature(job[0])
                args = []
                for i in range(len(sig.parameters)):
                    args.append(job[i+1])
                result = job[0](*args)
                if inspect.isawaitable(result):
                    if result.__name__.endswith('_'):
                        asyncio.create_task(result)
                    else:
                        await result

class PriorityCoroutine:

    def __init__(self, coroutine: Coroutine):
        self.coroutine = coroutine

async def main(loop):

    client: TelegramClient
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH, system_version="4.16.30-vxCUSTOM", auto_reconnect=True) as client:

        app = App(client = client, loop = loop)
        app.setup()
        app.draw()
        await app.start()

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(main(event_loop))