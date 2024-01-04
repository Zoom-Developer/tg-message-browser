from enum import Enum
import dearpygui.dearpygui as dpg

class ThemeService:

    def setupThemes(self):

        with dpg.theme() as self.mainTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 2, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 4.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3, category=dpg.mvThemeCat_Core)
                # dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 13.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 8.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 1.0, category=dpg.mvThemeCat_Core)
                # dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 4.0, category=dpg.mvThemeCat_Core)
                # dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3.5, category=dpg.mvThemeCat_Core)
                # dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)

                dpg.add_theme_color(dpg.mvThemeCol_Text, [204.0, 204.0, 211.64999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, [61.199999999999996, 58.650000000000006, 73.94999999999999, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [25, 25, 35, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [25, 25, 35, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, [25, 25, 35, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Border, [204.0, 204.0, 211.64999999999998, 224.4], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, [234.60000000000002, 232.05, 224.4, 0.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [40, 40, 50, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, [61.199999999999996, 58.650000000000006, 73.94999999999999, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, [142.8, 142.8, 147.89999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, [193.8, 79.05, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, [255.0, 249.9, 242.25, 191.25], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, [204.0, 84.15, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, [25.5, 22.95, 30.599999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, [25.5, 22.95, 30.599999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, [193.8, 79.05, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, [193.8, 79.05, 0.0, 127.5], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, [193.8, 79.05, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, [255.0, 107.1, 0.0, 135.15], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, [193.8, 79.05, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, [193.8, 79.05, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Button, [40, 40, 60, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [61.199999999999996, 58.650000000000006, 73.94999999999999, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [142.8, 142.8, 147.89999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Header, [40.0, 40.0, 50.0, 255.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, [142.8, 142.8, 147.89999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, [15.299999999999999, 12.75, 17.85, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, [0.0, 0.0, 0.0, 0.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, [142.8, 142.8, 147.89999999999998, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, [15.299999999999999, 12.75, 17.85, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PlotLines, [102.0, 99.45, 96.9, 160.65], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, [63.75, 255.0, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, [102.0, 99.45, 96.9, 160.65], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, [63.75, 255.0, 0.0, 255.0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, [63.75, 255.0, 0.0, 109.64999999999999], category=dpg.mvThemeCat_Core)

        self.colors = RGBColors

        with dpg.theme() as self.usersTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [16, 16, 16], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.contentTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [33, 33, 33], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.dialogTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [193, 79, 0], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.replayTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [22, 22, 22], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.contextTheme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [90, 90, 90], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.transparentButton:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 0, 0, 0], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.loadButton:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [21, 146, 70], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [20, 176, 82], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [14, 103, 49], category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.resetButton:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [187, 18, 18], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [208, 31, 31], category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [149, 16, 16], category=dpg.mvThemeCat_Core)

    def bindTheme(self):

        dpg.bind_theme(self.mainTheme)

class RGBColors(str, Enum):

    Selection = "{CD780D}"
    Text = "{A8A8A8}"
    Timestamp = "{9B9B9B}"
    Media = "{0C64BD}"