from dataclasses import dataclass


@dataclass
class FilmInfo:
    """Film info dataclass."""

    film_id: str
    film_title: str
    film_alternate_title: str
    film_year: str


@dataclass
class FilmInfoNoAlternate:
    """ "Film info dataclass without alternate title."""

    film_id: str
    film_title: str
    film_year: str
