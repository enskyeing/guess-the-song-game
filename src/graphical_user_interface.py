import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

# ======= UI STYLE CONSTANTS ========
# BG = tk.PhotoImage(file="assets/music-bg.png")
DEFAULT_FONT = ("ROBOTO", 16, "bold")


class UserInterface(ctk.CTk):
    def __init__(self) -> None:
        super().__init__(fg_color="#8B80F9")

        # App Config
        self.title = "Guess the Song"
        self.geometry("900x550")
        ctk.set_default_color_theme("src/theme.json")

        # Page
        self.home_page()

    def home_page(self):
        # Divider Frames
        top_frame = ctk.CTkFrame(
            self,
            width=900,
            height=350,
            fg_color="transparent"
        )
        top_frame.grid(column=0, columnspan=5, row=0, rowspan=3)

        # Buttons
        sp_btn = ctk.CTkButton(
            self, 
            text="SINGLEPLAYER", 
            font=DEFAULT_FONT,
            width=200,
            height=50
            )
        
        sp_btn.grid(column=1, row=3)

        mp_btn = ctk.CTkButton(
            self, 
            text="MULTIPLAYER", 
            font=DEFAULT_FONT,
            text_color="#000000",
            fg_color="#6CD4FF",
            hover_color="#7CAAFC",
            border_color="#7CAAFC",
            border_width=1,
            width=200,
            height=50
            )
        
        mp_btn.grid(column=3, row=3)

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
