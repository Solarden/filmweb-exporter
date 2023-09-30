from typing import Dict
from typing import Optional
from typing import Union

from requests import RequestException
from requests import Response
from requests import Session

from connectors.filmweb.exceptions import FilmwebConnectionError
from core import settings


class FilmwebConnector:
    """Connector for Filmweb."""

    USER_FILMS_URL: str = "user/{username}/films?page={page}"
    USER_FILM_RATING_URL: str = "logged/vote/film/{film_id}/details"

    def __init__(self, username: Optional[str] = None, user_cookie: Optional[str] = None, timeout: int = 10) -> None:
        self.cookie = user_cookie
        self.username = username
        self.timeout = timeout
        self._session = Session()

    def update_cookie(self, user_cookie: str) -> None:
        """Update cookie."""
        self.cookie = user_cookie

    def update_username(self, username: str) -> None:
        """Update username."""
        self.username = username

    def _request(
        self,
        *,
        method: str,
        path: str,
        filmweb_url: str = settings.FILMWEB_API_URL,
        headers: Dict[str, Union[str, int]] = None,
        data: Dict[str, str] = None,
        json: Dict[str, str] = None,
        params: Dict[str, str] = None,
    ) -> Response:
        """Request to Filmweb."""
        url = filmweb_url + path
        headers = headers or {}
        headers["Cookie"] = self.cookie

        try:
            response: Response = self._session.request(
                method=method, url=url, timeout=self.timeout, headers=headers, data=data, json=json, params=params
            )
            response.raise_for_status()
        except RequestException as exc:
            raise FilmwebConnectionError(message="Error occurred when connecting to Filmweb.") from exc

        return response

    def get_user_films(self, page: int = 1) -> str:
        """Get user films."""
        response = self._request(
            method="GET",
            filmweb_url=settings.BASE_FILMWEB_URL,
            path=self.USER_FILMS_URL.format(username=self.username, page=page),
        )
        return response.text
