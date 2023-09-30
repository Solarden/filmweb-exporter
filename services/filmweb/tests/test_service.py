from unittest.mock import patch

from scrappers.filmweb.tests.examples import example as example_response
from services.filmweb.service import FilmwebService


def test_service_correctly_gets_data_and_saves_to_database():
    service = FilmwebService("Solard")
    with patch("connectors.filmweb.connector.FilmwebConnector.get_user_films") as connector_mock:
        connector_mock.return_value = example_response
        service_result = service.get_user_films()

    assert service_result
    assert len(service_result) == 25

    assert service.database.database
    assert len(service.database.database) == 25

    for result in service_result:
        assert result.film_id in service.database.database
        assert service.database.database[result.film_id]["film_id"] == result.film_id
        assert service.database.database[result.film_id]["film_title"] == result.film_title
        assert service.database.database[result.film_id]["film_year"] == result.film_year

        if hasattr(result, "film_alternate_title"):
            assert service.database.database[result.film_id]["film_alternate_title"] == result.film_alternate_title
        else:
            assert service.database.database[result.film_id]["film_alternate_title"] is None
