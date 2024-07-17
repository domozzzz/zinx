from bs4 import BeautifulSoup
import urllib.request
import requests
import os
from threading import Thread


def download_thread(app, url, file_location):
    if not url.startswith('http'):
        url = 'https://' + url

    if url[-1] != '/':
        url += '/'

    dl_thread = Thread(target=download, args=(app, url, file_location))
    dl_thread.start()

def download(app, url, file_location):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    imgs = soup.find_all("img")
    app.set_total(len(imgs))

    for i, img in enumerate(imgs):
        app.print_progress(i+1)

        img_url = img['src']
        if not img_url.startswith('http'):  # Handle relative URLs
            img_url = urllib.parse.urljoin(url, img_url)

        print(file_location + os.path.basename(img_url))

        urllib.request.urlretrieve(url + imgs[i]['src'] , f"{file_location}{os.path.basename(img_url)}")