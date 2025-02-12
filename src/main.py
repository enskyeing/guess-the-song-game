from dotenv import dotenv_values
from game_brain import *

config = dotenv_values(".env")


TIME_LIMIT = 60


if __name__ == "__main__":
    game = GTSGame(genius_key=config["GENIUS_CLIENT_ACCESS_TOKEN"], time_limit=TIME_LIMIT)
