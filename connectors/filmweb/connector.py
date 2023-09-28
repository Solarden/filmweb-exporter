import settings
from requests import Session


class FilmwebConnector:
    """Connector for Filmweb."""

    def __init__(self, timeout: int = 10) -> None:
        self.timeout = timeout
        self._url = settings.FILMWEB_API_URL
        self._session = Session()

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate user."""
        self._session.auth = (username, password)
