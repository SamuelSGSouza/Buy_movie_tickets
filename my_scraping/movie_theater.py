from my_scraping.day_of_session import MoviesOfTheDay, Movie
from selenium.webdriver.common.by import By
from datetime import datetime
from my_scraping.utils.browsers import MyBrowser, ChromeBrowser
from typing import Dict


class MovieTheater:
    def __init__(self, root_link: str,) -> None:
        self.browser = ''
        self.root_link = root_link
        self.days_of_sessions_disponible = []
        self.data_to_movieOfDay_dict = {}

    def browser_get_link(self, link: str) -> None:
        self.browser.get(link)

    def get_disponible_days_of_sessions(self, ) -> list:
        '''This function find the dates disponible with sessions
        at the selected movie theater'''
        self.browser_get_link(self.root_link)
        dates = [date.text for date in self.browser.find_elements(
            By.CLASS_NAME,
            'date-main-info')
        ]
        # this action must be done else not all dates will be get
        try:
            self.browser.find_element(
                By.CLASS_NAME, 'swiper-button-next').click()
            for date in self.browser.find_elements(By.CLASS_NAME, 'date-main-info'):
                dates.append(date.text)
            self.browser.find_element(
                By.CLASS_NAME, 'swiper-button-next').click()
            for date in self.browser.find_elements(By.CLASS_NAME, 'date-main-info'):
                if date.text not in dates:
                    dates.append(date.text)
        except:
            pass
        # end_action

        self.days_of_sessions_disponible = list(
            filter(None, list(dict.fromkeys(dates))))

    def generate_dict_date_to_link(self) -> dict:
        date_to_link = {}
        for date in self.days_of_sessions_disponible:
            date_n = date.split('/')
            date_n = date_n[-1] + date_n[0]
            link = self.root_link + '#!#data=' + \
                f'{datetime.now().year}' + f'{date_n}'
            date_to_link[date] = link
        return date_to_link

    def make_date_to_movie_dict(self) -> dict:
        dates_to_links = self.generate_dict_date_to_link()
        for date, link in dates_to_links.items():
            self.browser_get_link(link)
            motd = MoviesOfTheDay(self.browser)
            self.data_to_movieOfDay_dict[date] = motd
        return self.data_to_movieOfDay_dict

    def make_browser(self, options: tuple) -> MyBrowser:
        self.browser = ChromeBrowser.make_browser(*options)
        return self.browser

    def find_film(self, required_movie_name: str) -> Dict[str, Movie]:
        for dia, movie in self.data_to_movieOfDay_dict.items():
            filme_achado = movie.search_films('ven')
            if filme_achado:
                filme_achado = {dia: filme_achado}
                return filme_achado
        return 'Movie not found!'
