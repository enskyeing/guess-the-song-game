from genius_brain import *
from data_managers import Artist, Song
import random
import time
import threading


class GTSGame:
    def __init__(self, genius_key: str, time_limit: int = 60):
        self.time_limit = time_limit
        self.genius = GeniusAPI(key=genius_key)
        self.artist = None
        self.song = None
        self.lyric = ""

        self.game_ongoing = True
        self.user_guessing = True
        self.timer_incomplete = True
        self.time_count = 0

        # game stats
        self.round: int = 0
        self.guess_times: list = []
        self.fastest_guess: tuple # (song name, time)
        self.artists_played: set = ()
        self.correct_guesses: int = 0
        

        self.welcome()
        self.start()

    def start_timer(self) -> None:
        self.time_count = self.time_limit
        self.timer_incomplete = True
        while self.timer_incomplete:
            time.sleep(1)
            self.time_count -= 1
            if self.time_count == 0:
                self.timer_incomplete = False
                print(f"Uh, oh! Time is up! The correct answer was '{self.song.title}'. Click enter to continue.")
            elif self.user_guessing is False:
                self.time_count = 0
                break

    def welcome(self):
        """Sends heading and game instructions."""
        gts_caps_ascii = r"""
           _____   _    _   ______    _____    _____       _______   _    _   ______        _____    ____    _   _    _____ 
          / ____| | |  | | |  ____|  / ____|  / ____|     |__   __| | |  | | |  ____|      / ____|  / __ \  | \ | |  / ____|
         | |  __  | |  | | | |__    | (___   | (___          | |    | |__| | | |__        | (___   | |  | | |  \| | | |  __ 
         | | |_ | | |  | | |  __|    \___ \   \___ \         | |    |  __  | |  __|        \___ \  | |  | | | . ` | | | |_ |
         | |__| | | |__| | | |____   ____) |  ____) |        | |    | |  | | | |____       ____) | | |__| | | |\  | | |__| |
          \_____|  \____/  |______| |_____/  |_____/         |_|    |_|  |_| |______|     |_____/   \____/  |_| \_|  \_____|
          """
        welcome_text = (
            f"Welcome to Guess the Song; the game where you need to guess which song the lyric belongs to within "
            f"{self.time_limit} seconds!")
        print(gts_caps_ascii + "\n" + welcome_text)

    def start(self):
        """Starts the game."""
        while self.game_ongoing:
            self.round += 1
            self.user_guessing = True
            self.choose_artist()
            self.choose_song()
            print(f"Round {self.round} starting in...")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            print("-------------------------------------")
            print(f"Artist: {self.artist.name}")
            print(f"Lyric: {self.choose_lyric()}")
            print("-------------------------------------")
            print(f"You have {self.time_limit} seconds, GO!")
            time_thread = threading.Thread(target=self.start_timer)
            time_thread.start()
            while self.time_count > 0:
                guess = input("Guess: ").lower()
                if guess == self.song.title.lower():
                    print(f"You guessed correctly!\nThe song was {self.song.title} by {self.artist.name}.")
                    self.user_guessing = False
                    time.sleep(1)  # wait for timer to reset
                elif guess == "q" or guess == "quit":
                    self.quit()
                    self.user_guessing = False
                    self.game_ongoing = False
                    break
                else:
                    continue
            if self.game_ongoing:
                self.replay()

    def replay(self):
        """Checks if player wants to play again."""
        valid_answer = False
        while not valid_answer:
            play_again = input("Would you like to play again? (y/n) ").lower()
            if play_again == "y":
                valid_answer = True
                self.game_ongoing = True
            elif play_again == "n" or play_again == "q" or play_again == "quit":
                valid_answer = True
                self.game_ongoing = False
                self.end()
            else:
                print("That was not a valid answer.")

    def quit(self):
        """Quit sequence"""
        while True:
            quit_game = input("Are you sure you want to quit? (y/n) ")
            if quit_game == "y":
                self.end()
                break
            elif quit_game != "y" and quit_game != "n":
                continue
            else:
                break

    def end(self):
        print(f"You played {self.round} round(s).\nThanks for playing Guess the Song!")

    def choose_artist(self):
        """Uses LyricGenius to get artist information and songs."""
        user_input = input("What musician would you like to play for this round? ")
        print(f"Searching for {user_input}...")
        artist_info = self.genius.get_artist(name=user_input)
        artist_songs = self.genius.get_artist_songs(artist_id=artist_info["id"])

        # Create Artist class with all the information of the selected artist
        self.artist = Artist(
            name=artist_info['name'],
            genius_id=artist_info['id'],
            songs=artist_songs,
            image=artist_info['image_url'],
            genius_link=artist_info['url']
        )
        print(f"{self.artist.name} found!")

    def choose_song(self):
        print("Choosing lyric...")
        random_song = random.choice(self.artist.songs)
        lyrics = self.genius.get_lyrics(song_id=random_song["id"])

        # Format data in Song class
        self.song = Song(
            title=random_song["title"].replace("\u200b", ""),
            lyrics=lyrics,
            cover=random_song['song_art_image_url'],
            genius_link=random_song['url'],
            genius_id=random_song['id']
        )

    def choose_lyric(self):
        lyric_list = [line for line in self.song.lyrics.splitlines() if len(line) > 25 and self.song.title not in line]
        return random.choice(lyric_list)