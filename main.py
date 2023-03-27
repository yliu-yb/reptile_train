import os
import requests
from bs4 import BeautifulSoup

url = "http://www.yinsuge.com/list/214-0-0-0-0.html"
os.makedirs("./video", exist_ok=True)

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
video_url = soup.find_all('source')
count = 0
titles = soup.find_all('a')
titles_str = []
for title in titles:
    if 'title' and 'target' and 'class' in title.attrs:
        if title.attrs['class'][0] == 'title':
            titles_str.append(title.attrs['title'])

for url, title in zip(video_url, titles_str):
    print(url)
    print(title)
    video = 'http://www.yinsuge.com' + url['src']
    print(video)
    video_request = requests.get(video)
    with open("./video/"+str(title)+".mp3", 'wb') as file:
        file.write(video_request.content)
    file.close()
    count+=1
    print("download ok")
