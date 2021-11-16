from typing import Dict, NewType
from selenium.webdriver.common.by import By

web_element = NewType('web_element', str)


class Sessions:
    def __init__(self, movie_box: web_element) -> None:
        self._sessions = {}
        self.movie_box = movie_box

        def get_sessions_hours(class_name_session: str = 'btn-primary') -> Dict[str, web_element]:
            sessoes = self.movie_box.find_elements(
                By.CLASS_NAME, class_name_session)
            for session in sessoes:
                if session.text != '':
                    self._sessions[session.text] = session
        get_sessions_hours()

    @property
    def sessions(self):
        return self._sessions

    @sessions.setter
    def sessions(self):
        return self._sessions

    def click_session(self, selected_session: int) -> None:
        '''
        This function receives an integer number and uses it as selector in the
        list of sessions. At the end the "click()" function from ChromeBrowser
        is called using the selected element from the list of sessions.
        '''
        s_session = self.get_sessions_lenght(selected_session)
        [session for session in self._sessions.values()][s_session].click()

    def get_sessions_lenght(self, s_session: int) -> int:
        '''
        This function garantees that if the number of the section selected isn't
        at the list, return the last session ate the list.
        '''
        if s_session >= len(self._sessions):
            s_session = len(self._sessions) - 1

        return s_session

    def __str__(self) -> str:
        horarios = [v for v in self._sessions.keys()]
        return f'{horarios}'
