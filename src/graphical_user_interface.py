import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk

# ======= UI STYLE CONSTANTS ========
TITLE_FONT = ("ARIAL", 60, "bold")
DEFAULT_FONT = ("CALIBRI", 20, "bold")
BG = "assets/music-bg-3.png"


class UserInterface(ctk.CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#1E0254")

        # App Config
        self.title("Guess the Song")
        self.geometry("900x550")
        ctk.set_default_color_theme("src/theme.json")

        # Background
        self.bg = tk.PhotoImage(file=BG)
        self.canvas_bg = ctk.CTkCanvas(
            self,
            width=900,
            height=550,
            highlightthickness=0,
            bg="#1E0254"
            )
        self.canvas_bg.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas_bg.grid(column=0, columnspan=5, row=0, rowspan=6)
        

        # Page
        self.home_page()

    def home_page(self):
        # TODO: Add removal of widgets from parent

        # Labels
        game_title = ctk.CTkLabel(
            master=self,
            text="GUESS THE SONG",
            font=TITLE_FONT,
            text_color="black"
        )
        self.canvas_bg.create_text(450, 250, text="GUESS THE\nSONG", font=TITLE_FONT, anchor="center", justify="center", fill="#FFA400")

        # Buttons
        sp_btn = ctk.CTkButton(
            self, 
            text="SINGLEPLAYER", 
            font=DEFAULT_FONT,
            width=200,
            height=50
            )
        self.canvas_bg.create_window(150, 400, anchor="nw", window=sp_btn)

        mp_btn = ctk.CTkButton(
            self, 
            text="MULTIPLAYER", 
            font=DEFAULT_FONT,
            width=200,
            height=50
            )
        self.canvas_bg.create_window(550, 400, anchor="nw", window=mp_btn)

        settings_icon = ctk.CTkImage(Image.open("assets/settings-icon.png"), size=(35, 35))
        settings_btn = ctk.CTkButton(
            self,
            text="",
            width=50,
            height=50,
            image=settings_icon
        )
        self.canvas_bg.create_window(800, 50, anchor="nw", window=settings_btn)

    def in_game_page(self):
        pass

    def sp_loading_page(self):
        pass

    def game_setup_page(self):
        pass

    def mp_lobby_page(self):
        pass

    def mp_loading_page(self):
        pass

    def _remove_all_children(self):
        pass

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
