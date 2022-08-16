from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
complete_movie_list = soup.find_all(name="h3", class_="title")

top100_movies_list = [movie_title.get_text() for movie_title in complete_movie_list]

top100_movies_list.reverse()

for movie in top100_movies_list:
    with open("movies_list.txt", "a", encoding="utf8") as movie_data:
        movie_data.write(f"{movie}\n")



