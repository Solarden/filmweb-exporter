from typing import List
from typing import Optional
from typing import Union

from connectors.filmweb.connector import FilmwebConnector
from scrappers.filmweb.scrapper import FilmInfo
from scrappers.filmweb.scrapper import FilmInfoNoAlternate
from scrappers.filmweb.scrapper import FilmwebScrapper


class FilmwebService:
    """Service class for Filmweb Site"""

    def __init__(self, username: Optional[str] = None) -> None:
        self._filmweb_connector = FilmwebConnector(username=username, timeout=10)

    def update_username(self, username: str) -> None:
        """Update username."""
        self._filmweb_connector.update_username(username)

    def update_cookie(self, user_cookie: str) -> None:
        """Update cookie."""
        self._filmweb_connector.update_cookie(user_cookie)

    def get_user_films(self, page: int = 1) -> List[Optional[Union[FilmInfo, FilmInfoNoAlternate]]]:
        """Get user films."""
        response: str = self._filmweb_connector.get_user_films(page=page)
        return FilmwebScrapper.get_any_filmweb_movie_info(response)
