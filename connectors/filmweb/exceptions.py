from common.exceptions import BasicException


class FilmwebConnectionError(BasicException):
    """Error occurred when connecting to Filmweb."""

    detail: str
