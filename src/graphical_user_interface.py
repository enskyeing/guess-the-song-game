import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

# ======= UI STYLE CONSTANTS ========


class UserInterface(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        # App Config
        self.title = "Guess the Song"
        self.geometry("900x550")

        # Page
        self.home_page()

    def home_page(self):
        pass

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
