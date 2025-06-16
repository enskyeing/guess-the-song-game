import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk

# ======= UI STYLE CONSTANTS ========
TITLE_FONT = ("ROBOTO", 60, "bold")
DEFAULT_FONT = ("ROBOTO", 16, "bold")


class UserInterface(ctk.CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#8B80F9")

        # App Config
        self.title("Guess the Song")
        self.geometry("900x550")
        ctk.set_default_color_theme("src/theme.json")

        # Background
        self.bg = tk.PhotoImage(file="assets/music-bg-2.png")
        self.canvas_bg = ctk.CTkCanvas(
            self,
            width=900,
            height=550,
            highlightthickness=0,
            bg="#1E0254"
            )
        self.main_frame = ctk.CTkFrame(
            self.canvas_bg, 
            width=900, 
            height=550, 
            fg_color="transparent"
            )
        self.canvas_bg.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas_bg.create_window(0, 0, window=self.main_frame, anchor="nw")
        self.canvas_bg.grid(column=0, columnspan=5, row=0, rowspan=6)
        

        # Page
        self.home_page()

    def home_page(self):
        # TODO: Add removal of widgets from parent

        # Divider Frames
        top_frame = ctk.CTkFrame(
            self.main_frame,
            width=900,
            height=350,
            fg_color="transparent"
        )
        top_frame.grid(column=0, columnspan=5, row=0, rowspan=3)

        # Labels
        game_title = ctk.CTkLabel(
            master=self.main_frame,
            text="GUESS THE SONG",
            font=TITLE_FONT,
            text_color="black"
        )
        game_title.grid(column=1, columnspan=3, row=1)

        # Buttons
        sp_btn = ctk.CTkButton(
            self.main_frame, 
            text="SINGLEPLAYER", 
            font=DEFAULT_FONT,
            width=200,
            height=50
            )
        sp_btn.grid(column=1, row=3)

        mp_btn = ctk.CTkButton(
            self.main_frame, 
            text="MULTIPLAYER", 
            font=DEFAULT_FONT,
            width=200,
            height=50
            )
        mp_btn.grid(column=3, row=3)

        settings_icon = ctk.CTkImage(Image.open("assets/settings-icon.png"), size=(35, 35))
        settings_btn = ctk.CTkButton(
            self.main_frame,
            text="",
            width=50,
            height=50,
            image=settings_icon
        )
        settings_btn.grid(column=4, row=0)

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
