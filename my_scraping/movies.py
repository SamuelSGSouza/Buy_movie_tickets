from typing import NewType
from my_scraping.sessions import Sessions
from selenium.webdriver.common.by import By

web_element = NewType('web_element', str)


class Movie:
    def __init__(self, movie_box: web_element) -> None:
        self.movie_box = movie_box
        self.movie_name = self.movie_box.find_element(
            By.CLASS_NAME, 'valign-middle').text
        self.duration = self.movie_box.find_element(
            By.CLASS_NAME, 'se-classification').text
        self.disponible_sessions = Sessions(self.movie_box)

    def select_session(self, selected_session: int):
        self.disponible_sessions.click_session(selected_session)

    def __str__(self):
        return self.movie_name
