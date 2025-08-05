"""
Musical Time Machine
Scrape Billboard and add the top 100 songs to a
Spotify Playlist

Beautiful Soup
Spotify api
"""
import requests
from bs4 import BeautifulSoup

chosen_date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 CCleaner/137.0.0.0'}
url = 'https://www.billboard.com/charts/hot-100/'+chosen_date+'/'
response = requests.get(url, headers=header)

page = response.text
soup = BeautifulSoup(page, 'html.parser')

# titles = soup.find_all(name='h3', id='title-of-a-story')
# song_titles = []
# for title in titles:
#     title = title.text
#     song_titles.append(title)
# print(song_titles)
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
