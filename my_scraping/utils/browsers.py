from selenium import webdriver
from selenium.webdriver.chrome.service import Service as google_service
from selenium.webdriver.firefox.service import Service as firefox_service
from abc import ABC, abstractmethod
from .paths import drivers


class MyBrowser(ABC):
    @abstractmethod
    def make_browser(*options: str) -> webdriver: pass


class ChromeBrowser(MyBrowser):

    def make_browser(*options) -> webdriver:
        driver_options = webdriver.ChromeOptions()
        if options is not None:
            for option in options:
                driver_options.add_argument(option)

        driver_service = google_service(
            executable_path=drivers['chrome']
        )

        browser = webdriver.Chrome(
            service=driver_service,
            options=driver_options
        )

        return browser


class FirefoxBrowser(MyBrowser):

    def make_browser(*options) -> webdriver:
        driver_options = webdriver.FirefoxOptions()
        if options is not None:
            for option in options:
                driver_options.add_argument(option)

        driver_service = firefox_service(
            executable_path=drivers['firefox']
        )

        browser = webdriver.Chrome(
            service=driver_service,
            options=driver_options
        )

        return browser
