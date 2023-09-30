from typing import List
from typing import Optional
from typing import Union

from common.models import FilmInfo
from common.models import FilmInfoNoAlternate
from connectors.filmweb.connector import FilmwebConnector
from core.database import FilmwebDatabase
from scrappers.filmweb.scrapper import FilmwebScrapper


class FilmwebService:
    """Service class for Filmweb Site"""

    def __init__(self, username: Optional[str] = None) -> None:
        self._filmweb_connector = FilmwebConnector(username=username, timeout=10)
        self.database = FilmwebDatabase()

    def update_username(self, username: str) -> None:
        """Update username."""
        self._filmweb_connector.update_username(username)

    def update_cookie(self, user_cookie: str) -> None:
        """Update cookie."""
        self._filmweb_connector.update_cookie(user_cookie)

    def get_user_films(self, page: int = 1) -> List[Optional[Union[FilmInfo, FilmInfoNoAlternate]]]:
        """Get user films."""
        response: str = self._filmweb_connector.get_user_films(page=page)
        scrapper_response = FilmwebScrapper.get_any_filmweb_movie_info(response)
        self.database.add_film_info(scrapper_response)
        return scrapper_response
