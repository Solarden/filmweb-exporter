from typing import List

from common.models import FilmInfo
from common.models import FilmInfoNoAlternate
from scrappers.filmweb.scrapper import FilmwebScrapper
from scrappers.filmweb.tests.examples import example


def test_scrapper_correctly_gets_film_ids():
    expected_result: List[str] = [
        "757778",
        "836440",
        "236351",
        "681141",
        "707970",
        "989",
        "1099",
        "120986",
        "733823",
        "706297",
        "790542",
        "714192",
        "871659",
        "76",
        "32237",
        "464231",
        "1301",
        "630798",
        "797011",
        "788329",
        "842452",
        "830631",
        "188890",
        "722146",
        "726369",
    ]
    results = FilmwebScrapper.get_filmweb_movie_ids(example)
    assert results == expected_result
    assert len(results) == 25


def test_scrapper_correctly_gets_film_titles():
    expected_result: List[str] = [
        "Nie czas umierać",
        "Doktor Strange w multiwersum obłędu",
        "Mroczny Rycerz",
        "Dunkierka",
        "Thor: Ragnarok",
        "Trainspotting",
        "Żywot Briana",
        "Czarna Wdowa",
        "The Ridiculous 6",
        "Magik z Nowego Jorku",
        "Avengers: Koniec gry",
        "Nienawistna &oacute;semka",
        "Zab&oacute;jcze złudzenia",
        "Jutro nie umiera nigdy",
        "Śmierć nadejdzie jutro",
        "Megan Is Missing",
        "Skrzypek na dachu",
        "Blade Runner 2049",
        "Unacknowledged",
        "Pierwsza noc oczyszczenia",
        "365 dni",
        "Tylko nie m&oacute;w nikomu",
        "Dawca pamięci",
        "Strażnicy Galaktyki vol. 2",
        "Nie otwieraj oczu",
    ]
    results = FilmwebScrapper.get_filmweb_movie_titles(example)
    assert results == expected_result
    assert len(results) == 25


def test_scrapper_correctly_gets_film_alternate_titles():
    expected_result: List[str] = [
        "No Time to Die",
        "Doctor Strange in the Multiverse of Madness",
        "The Dark Knight",
        "Dunkirk",
        "Life of Brian",
        "Black Widow",
        "The Cobbler",
        "Avengers: Endgame",
        "The Hateful Eight",
        "Deadly Illusions",
        "Tomorrow Never Dies",
        "Die Another Day",
        "Fiddler on the Roof",
        "The First Purge",
        "The Giver",
        "Guardians of the Galaxy Vol. 2",
        "Bird Box",
    ]
    results = FilmwebScrapper.get_filmweb_movie_alternate_titles(example)
    assert results == expected_result
    assert len(results) == 17


def test_scrapper_correctly_gets_film_years():
    expected_result: List[str] = [
        "2021",
        "2022",
        "2008",
        "2017",
        "2017",
        "1996",
        "1979",
        "2021",
        "2015",
        "2014",
        "2019",
        "2015",
        "2021",
        "1997",
        "2002",
        "2011",
        "1971",
        "2017",
        "2017",
        "2018",
        "2020",
        "2019",
        "2014",
        "2017",
        "2018",
    ]
    results = FilmwebScrapper.get_filmweb_movie_years(example)
    assert results == expected_result
    assert len(results) == 25


def test_scrapper_correctly_gets_film_info():
    expected_result = [
        FilmInfo(
            film_id="757778",
            film_title="Nie czas umierać",
            film_alternate_title="No Time to Die",
            film_year="2021",
        ),
        FilmInfo(
            film_id="836440",
            film_title="Doktor Strange w multiwersum obłędu",
            film_alternate_title="Doctor Strange in the Multiverse of Madness",
            film_year="2022",
        ),
        FilmInfo(
            film_id="236351",
            film_title="Mroczny Rycerz",
            film_alternate_title="The Dark Knight",
            film_year="2008",
        ),
        FilmInfo(
            film_id="681141",
            film_title="Dunkierka",
            film_alternate_title="Dunkirk",
            film_year="2017",
        ),
        FilmInfo(
            film_id="1099",
            film_title="Żywot Briana",
            film_alternate_title="Life of Brian",
            film_year="1979",
        ),
        FilmInfo(
            film_id="120986",
            film_title="Czarna Wdowa",
            film_alternate_title="Black Widow",
            film_year="2021",
        ),
        FilmInfo(
            film_id="706297",
            film_title="Magik z Nowego Jorku",
            film_alternate_title="The Cobbler",
            film_year="2014",
        ),
        FilmInfo(
            film_id="790542",
            film_title="Avengers: Koniec gry",
            film_alternate_title="Avengers: Endgame",
            film_year="2019",
        ),
        FilmInfo(
            film_id="714192",
            film_title="Nienawistna &oacute;semka",
            film_alternate_title="The Hateful Eight",
            film_year="2015",
        ),
        FilmInfo(
            film_id="871659",
            film_title="Zab&oacute;jcze złudzenia",
            film_alternate_title="Deadly Illusions",
            film_year="2021",
        ),
        FilmInfo(
            film_id="76",
            film_title="Jutro nie umiera nigdy",
            film_alternate_title="Tomorrow Never Dies",
            film_year="1997",
        ),
        FilmInfo(
            film_id="32237",
            film_title="Śmierć nadejdzie jutro",
            film_alternate_title="Die Another Day",
            film_year="2002",
        ),
        FilmInfo(
            film_id="1301",
            film_title="Skrzypek na dachu",
            film_alternate_title="Fiddler on the Roof",
            film_year="1971",
        ),
        FilmInfo(
            film_id="788329",
            film_title="Pierwsza noc oczyszczenia",
            film_alternate_title="The First Purge",
            film_year="2018",
        ),
        FilmInfo(
            film_id="188890",
            film_title="Dawca pamięci",
            film_alternate_title="The Giver",
            film_year="2014",
        ),
        FilmInfo(
            film_id="722146",
            film_title="Strażnicy Galaktyki vol. 2",
            film_alternate_title="Guardians of the Galaxy Vol. 2",
            film_year="2017",
        ),
        FilmInfo(
            film_id="726369",
            film_title="Nie otwieraj oczu",
            film_alternate_title="Bird Box",
            film_year="2018",
        ),
    ]
    results = FilmwebScrapper.get_filmweb_movie_info(example)
    assert results == expected_result
    assert len(results) == 17


def test_test_scrapper_correctly_gets_film_info_no_alternate():
    expected_result = [
        FilmInfoNoAlternate(film_id="757778", film_title="Nie czas umierać", film_year="2021"),
        FilmInfoNoAlternate(
            film_id="836440",
            film_title="Doktor Strange w multiwersum obłędu",
            film_year="2022",
        ),
        FilmInfoNoAlternate(film_id="236351", film_title="Mroczny Rycerz", film_year="2008"),
        FilmInfoNoAlternate(film_id="681141", film_title="Dunkierka", film_year="2017"),
        FilmInfoNoAlternate(film_id="707970", film_title="Thor: Ragnarok", film_year="2017"),
        FilmInfoNoAlternate(film_id="989", film_title="Trainspotting", film_year="1996"),
        FilmInfoNoAlternate(film_id="1099", film_title="Żywot Briana", film_year="1979"),
        FilmInfoNoAlternate(film_id="120986", film_title="Czarna Wdowa", film_year="2021"),
        FilmInfoNoAlternate(film_id="733823", film_title="The Ridiculous 6", film_year="2015"),
        FilmInfoNoAlternate(film_id="706297", film_title="Magik z Nowego Jorku", film_year="2014"),
        FilmInfoNoAlternate(film_id="790542", film_title="Avengers: Koniec gry", film_year="2019"),
        FilmInfoNoAlternate(film_id="714192", film_title="Nienawistna &oacute;semka", film_year="2015"),
        FilmInfoNoAlternate(film_id="871659", film_title="Zab&oacute;jcze złudzenia", film_year="2021"),
        FilmInfoNoAlternate(film_id="76", film_title="Jutro nie umiera nigdy", film_year="1997"),
        FilmInfoNoAlternate(film_id="32237", film_title="Śmierć nadejdzie jutro", film_year="2002"),
        FilmInfoNoAlternate(film_id="464231", film_title="Megan Is Missing", film_year="2011"),
        FilmInfoNoAlternate(film_id="1301", film_title="Skrzypek na dachu", film_year="1971"),
        FilmInfoNoAlternate(film_id="630798", film_title="Blade Runner 2049", film_year="2017"),
        FilmInfoNoAlternate(film_id="797011", film_title="Unacknowledged", film_year="2017"),
        FilmInfoNoAlternate(film_id="788329", film_title="Pierwsza noc oczyszczenia", film_year="2018"),
        FilmInfoNoAlternate(film_id="842452", film_title="365 dni", film_year="2020"),
        FilmInfoNoAlternate(film_id="830631", film_title="Tylko nie m&oacute;w nikomu", film_year="2019"),
        FilmInfoNoAlternate(film_id="188890", film_title="Dawca pamięci", film_year="2014"),
        FilmInfoNoAlternate(film_id="722146", film_title="Strażnicy Galaktyki vol. 2", film_year="2017"),
        FilmInfoNoAlternate(film_id="726369", film_title="Nie otwieraj oczu", film_year="2018"),
    ]
    results = FilmwebScrapper.get_filmweb_movie_info_no_alternate(example)
    assert results == expected_result
    assert len(results) == 25


def test_scrapper_correctly_gets_any_film_info():
    expected_result = [
        FilmInfo(
            film_id="757778",
            film_title="Nie czas umierać",
            film_alternate_title="No Time to Die",
            film_year="2021",
        ),
        FilmInfo(
            film_id="836440",
            film_title="Doktor Strange w multiwersum obłędu",
            film_alternate_title="Doctor Strange in the Multiverse of Madness",
            film_year="2022",
        ),
        FilmInfo(
            film_id="236351",
            film_title="Mroczny Rycerz",
            film_alternate_title="The Dark Knight",
            film_year="2008",
        ),
        FilmInfo(
            film_id="681141",
            film_title="Dunkierka",
            film_alternate_title="Dunkirk",
            film_year="2017",
        ),
        FilmInfoNoAlternate(film_id="707970", film_title="Thor: Ragnarok", film_year="2017"),
        FilmInfoNoAlternate(film_id="989", film_title="Trainspotting", film_year="1996"),
        FilmInfo(
            film_id="1099",
            film_title="Żywot Briana",
            film_alternate_title="Life of Brian",
            film_year="1979",
        ),
        FilmInfo(
            film_id="120986",
            film_title="Czarna Wdowa",
            film_alternate_title="Black Widow",
            film_year="2021",
        ),
        FilmInfoNoAlternate(film_id="733823", film_title="The Ridiculous 6", film_year="2015"),
        FilmInfo(
            film_id="706297",
            film_title="Magik z Nowego Jorku",
            film_alternate_title="The Cobbler",
            film_year="2014",
        ),
        FilmInfo(
            film_id="790542",
            film_title="Avengers: Koniec gry",
            film_alternate_title="Avengers: Endgame",
            film_year="2019",
        ),
        FilmInfo(
            film_id="714192",
            film_title="Nienawistna &oacute;semka",
            film_alternate_title="The Hateful Eight",
            film_year="2015",
        ),
        FilmInfo(
            film_id="871659",
            film_title="Zab&oacute;jcze złudzenia",
            film_alternate_title="Deadly Illusions",
            film_year="2021",
        ),
        FilmInfo(
            film_id="76",
            film_title="Jutro nie umiera nigdy",
            film_alternate_title="Tomorrow Never Dies",
            film_year="1997",
        ),
        FilmInfo(
            film_id="32237",
            film_title="Śmierć nadejdzie jutro",
            film_alternate_title="Die Another Day",
            film_year="2002",
        ),
        FilmInfoNoAlternate(film_id="464231", film_title="Megan Is Missing", film_year="2011"),
        FilmInfo(
            film_id="1301",
            film_title="Skrzypek na dachu",
            film_alternate_title="Fiddler on the Roof",
            film_year="1971",
        ),
        FilmInfoNoAlternate(film_id="630798", film_title="Blade Runner 2049", film_year="2017"),
        FilmInfoNoAlternate(film_id="797011", film_title="Unacknowledged", film_year="2017"),
        FilmInfo(
            film_id="788329",
            film_title="Pierwsza noc oczyszczenia",
            film_alternate_title="The First Purge",
            film_year="2018",
        ),
        FilmInfoNoAlternate(film_id="842452", film_title="365 dni", film_year="2020"),
        FilmInfoNoAlternate(film_id="830631", film_title="Tylko nie m&oacute;w nikomu", film_year="2019"),
        FilmInfo(
            film_id="188890",
            film_title="Dawca pamięci",
            film_alternate_title="The Giver",
            film_year="2014",
        ),
        FilmInfo(
            film_id="722146",
            film_title="Strażnicy Galaktyki vol. 2",
            film_alternate_title="Guardians of the Galaxy Vol. 2",
            film_year="2017",
        ),
        FilmInfo(
            film_id="726369",
            film_title="Nie otwieraj oczu",
            film_alternate_title="Bird Box",
            film_year="2018",
        ),
    ]

    results = FilmwebScrapper.get_any_filmweb_movie_info(example)
    assert results == expected_result
    assert len(results) == 25
