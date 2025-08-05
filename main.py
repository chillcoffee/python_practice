"""
Web Scraping using BeautifulSoup
Top 100 Movies from empireonline.com
"""

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
page = response.text
soup = BeautifulSoup(page, 'html.parser')

#titles sa loob ng div na may h3 na may class title
movie_titles = soup.find_all(name="h3", class_="title" )
movies = []
#loop get all titles
for movie in movie_titles:
    movies.append(movie.text)
movies.reverse()     # or do movies[::-1] #list_splicing



#write to file
with open("movies.txt", "a", encoding='utf8') as file:
    for movie in movies:
        file.write(movie + "\n")



