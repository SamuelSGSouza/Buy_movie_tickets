from typing import NewType
from selenium.webdriver.common.by import By
from my_scraping.movies import Movie
from my_scraping.utils.browsers import MyBrowser

web_element = NewType('web_element', str)


class MoviesOfTheDay:
    def __init__(self, browser: MyBrowser) -> None:
        self.movies = []
        self.browser = browser

        def make_movies_boxes(movie_box_className: str = 'box-tp2') -> list[web_element]:
            movie_boxes = self.browser.find_elements(
                By.CLASS_NAME, movie_box_className)
            for movie_box in movie_boxes:
                movie = Movie(movie_box)
                self.movies.append(movie)
        make_movies_boxes()

    def search_films(self, film_name: str) -> Movie:
        for movie in self.movies:
            if film_name in movie.movie_name.lower():
                return movie
        return None

    def __str__(self):
        string = ''
        for movie in self.movies:
            string = string + f'{movie}, '
        return string
