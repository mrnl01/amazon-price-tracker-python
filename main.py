import requests
from bs4 import BeautifulSoup

date=input("Which year do you want to travel to? Type the date in this format - 'yyyy-mm-dd'\n")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
}
url='https://www.billboard.com/charts/hot-100/' + date
response = requests.get(url=url,headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
# with open('html.txt','w') as file:
#     file.write(soup.prettify())
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)