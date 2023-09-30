import re
from typing import List
from typing import Optional
from typing import Union

from common.models import FilmInfo
from common.models import FilmInfoNoAlternate


class FilmwebScrapper:
    """Scrapper class for Filmweb Site"""

    MOVIE_IDS_REGEX = r"<span id=\"(?P<film_id>\d+)\"></span>"
    MOVIE_TITLE_REGEX = r"title=\"(?P<film_title>.*?)\"><div class=\"ribbon"
    MOVIE_ALTERNATE_TITLE_REGEX = r"preview__alternateTitle\">(?P<film_alternate_title>.*?)</div>"
    MOVIE_YEAR_REGEX = r"itemprop=\"datePublished\" content=\"\d+\">(?P<film_year>\d+)</div>"
    MOVIE_INFO_REGX = (
        r"data-film-id=\"(?P<film_id>\d+)\".*?title=\"(?P<film_title>.*?)\">.*?preview__alternateTitle\">"
        r"(?P<film_alternate_title>.*?)</div>.*?itemprop=\"datePublished\" content=\"\d+\">(?P<film_year>\d+)</div>"
    )
    MOVIE_INFO_NO_ALTERNATE_REGEX = (
        r"data-film-id=\"(?P<film_id>\d+)\".*?title=\"(?P<film_title>.*?)\">.*?itemprop=\"datePublished\" "
        r"content=\"\d+\">(?P<film_year>\d+)</div>"
    )

    @classmethod
    def get_filmweb_movie_ids(cls, page_content: str) -> List[Optional[str]]:
        """Get movie ids from filmweb page."""
        return re.findall(cls.MOVIE_IDS_REGEX, page_content)

    @classmethod
    def get_filmweb_movie_titles(cls, page_content: str) -> List[Optional[str]]:
        """Get movie titles from filmweb page."""
        return re.findall(cls.MOVIE_TITLE_REGEX, page_content)

    @classmethod
    def get_filmweb_movie_alternate_titles(cls, page_content: str) -> List[Optional[str]]:
        """Get movie alternate titles from filmweb page."""
        return re.findall(cls.MOVIE_ALTERNATE_TITLE_REGEX, page_content)

    @classmethod
    def get_filmweb_movie_years(cls, page_content: str) -> List[Optional[str]]:
        """Get movie years from filmweb page."""
        return re.findall(cls.MOVIE_YEAR_REGEX, page_content)

    @classmethod
    def get_filmweb_movie_info(cls, page_content: str) -> List[Optional[FilmInfo]]:
        """Get movie info from filmweb page."""
        return [FilmInfo(*movie_info) for movie_info in re.findall(cls.MOVIE_INFO_REGX, page_content)]

    @classmethod
    def get_filmweb_movie_info_no_alternate(cls, page_content: str) -> List[Optional[FilmInfoNoAlternate]]:
        """Get movie info from filmweb page without alternate title."""
        return [
            FilmInfoNoAlternate(*movie_info)
            for movie_info in re.findall(cls.MOVIE_INFO_NO_ALTERNATE_REGEX, page_content)
        ]

    @classmethod
    def get_any_filmweb_movie_info(cls, page_content: str) -> List[Optional[Union[FilmInfoNoAlternate, FilmInfo]]]:
        """Get movie info from filmweb page without alternate title."""
        full_info = cls.get_filmweb_movie_info(page_content)
        no_alternate_info = cls.get_filmweb_movie_info_no_alternate(page_content)
        if len(full_info) == len(no_alternate_info):
            return full_info

        any_info = []
        movie_ids_with_full_info = [movie.film_id for movie in full_info]
        for movie_with_no_alternate_info in no_alternate_info:
            if movie_with_no_alternate_info.film_id in movie_ids_with_full_info:
                any_info.append(full_info[movie_ids_with_full_info.index(movie_with_no_alternate_info.film_id)])
            else:
                any_info.append(movie_with_no_alternate_info)

        return any_info
