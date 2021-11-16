from pprint import pprint
from time import sleep
from movie_theater import MovieTheater


options = ('--disable-gpu', '--no-sandbox')
cinema = MovieTheater(
    'https://www.ingresso.com/cinema/gnc-garten-shopping?city=joinville')
browser = cinema.make_browser(options)
cinema.get_disponible_days_of_sessions()
cinema.generate_dict_date_to_link()
cinema.make_date_to_movie_dict()
print(cinema.find_film('ven'))
sleep(30)
browser.quit()
