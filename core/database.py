from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from common.models import FilmInfo
from common.models import FilmInfoNoAlternate


class Database:
    """Database class to store all the data"""

    database: Dict[str, Dict[str, Any]] = {}

    def add(self, key: str, value: Dict[str, Any]) -> None:
        """Add a key value pair to the database"""
        self.database[key] = value

    def get(self, key: str) -> Dict[str, Any]:
        """Get the value of a key from the database"""
        return self.database[key]

    def delete(self, key: str) -> None:
        """Delete a key from the database"""
        del self.database[key]


class FilmwebDatabase(Database):
    """Filmweb Database class to store all the data"""

    def add_film_info(self, scrapper_result: List[Optional[Union[FilmInfoNoAlternate, FilmInfo]]]) -> None:
        """Add film info to database"""
        for film_info in scrapper_result:
            self.add(
                film_info.film_id,
                {
                    "film_id": film_info.film_id,
                    "film_title": film_info.film_title,
                    "film_alternate_title": film_info.film_alternate_title
                    if hasattr(film_info, "film_alternate_title")
                    else None,
                    "film_year": film_info.film_year,
                },
            )
