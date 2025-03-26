from dataclasses import dataclass

@dataclass
class Artist:
    """Dataclass containing name, id, songs, image, and genius link for an Artist."""
    name: str
    id: int
    songs: list
    image: str
    genius_link: str


@dataclass
class Song:
    """Dataclass containing the title, lyrics, cover, genius link, and genius ID for a song."""
    title: str
    lyrics: str
    cover: str
    genius_link: str
    id: int