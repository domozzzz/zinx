from bs4 import BeautifulSoup
import urllib.request
import requests
import os
from threading import Thread


def download_thread(app, source_url, destination_path):
    # Ensure an http prefix
    if not source_url.startswith('http'):
        source_url = 'https://' + source_url

    # Ensure a trailing backslash for destination
    if source_url[-1] != '/':
        source_url += '/'

    dl_thread = Thread(target=download, args=(app, source_url, destination_path))
    dl_thread.start()

def download(app, source_url, destination_path):

    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, "html.parser")

    imgs = soup.find_all("img")
    app.set_progress_total(len(imgs))

    for i, img in enumerate(imgs):
        app.update_progress_bar(i + 1)

        img_url = img['src']
        if not img_url.startswith('http'):  # Handle relative URLs
            img_url = urllib.parse.urljoin(source_url, img_url)

        print(destination_path + os.path.basename(img_url))

        urllib.request.urlretrieve(source_url + imgs[i]['src'] , f"{destination_path}{os.path.basename(img_url)}")