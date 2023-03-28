import os
import requests
from bs4 import BeautifulSoup

url = "http://www.yinsuge.com/list/214-0-0-0-1.html"

def get_video_names_links():
    video_urls = []
    video_names = []
    # create response object
    html = requests.get(url).text
    # create beautiful-soup object
    soup = BeautifulSoup(html, 'html.parser')
    # find and save all video urls on web-page
    video_links = soup.find_all('source')
    for video_link in video_links:
        video_urls.append('http://www.yinsuge.com' + video_link['src'])
    # find and save all video names on web-page
    titles = soup.find_all('a')
    for title in titles:
        if 'title' and 'target' and 'class' in title.attrs:
            if title.attrs['class'][0] == 'title':
                video_names.append(title.attrs['title'])
    return video_names, video_urls

def download_video_series(video_names, video_urls):
    for url, name in zip(video_urls, video_names):
        '''iterate through all links in video_links 
                and download them one by one'''
        print("Downloading file:", name)
        # create response object
        r = requests.get(url, stream=True)
        # download started
        with open("./video/" + name + ".mp3", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                # writing one chunk at a time to video file
                if chunk:
                    f.write(chunk)
        print("%s downloaded!\n"%name)
    print("All videos downloaded!")

if __name__ == "__main__":
    os.makedirs("./video", exist_ok=True)

    # getting all video links
    video_names, video_links = get_video_names_links()

    # download all videos
    download_video_series(video_names, video_links)
