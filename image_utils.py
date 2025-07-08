import requests
import os
from pathlib import Path
from urllib.parse import urlsplit, unquote
from os.path import split, splitext


def get_file_extension(url):
    parsed_url = unquote(urlsplit(url).path)
    file_extension = splitext(split(parsed_url)[1])
    return file_extension[1]


def get_paths_images(path_dir):
    paths_all_images = []
    for dirpath, _, filenames in os.walk(path_dir):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            file_path = Path(dirpath) / filename
            paths_all_images.append(file_path)
    return paths_all_images


def download_img_for_url(img_url, path_dir, file_name, params=None):
    image_response = requests.get(img_url, params=params)
    image_response.raise_for_status()
    with open(path_dir / file_name, 'wb') as file:
        file.write(image_response.content)
