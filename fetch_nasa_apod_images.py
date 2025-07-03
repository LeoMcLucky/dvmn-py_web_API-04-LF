import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from get_file_data import get_file_extension


def fetch_nasa_images(url_NASA, api_key_NASA, path_dir):
    payload = {
        'api_key': api_key_NASA,
        'count': 30,
    }
    response = requests.get(url_NASA, params=payload)
    response.raise_for_status()
    img_urls = response.json()
    for number, img_url in enumerate(img_urls):
        file_ext = get_file_extension(img_url['hdurl'])
        image_response = requests.get(img_url['hdurl'])
        image_response.raise_for_status()
        with open(path_dir / f'NASA_{number}{file_ext}', 'wb') as file:
            file.write(image_response.content)


def main():
    load_dotenv()
    api_key_NASA = os.environ['API_KEY_NASA']
    url_NASA = 'https://api.nasa.gov/planetary/apod'
    path_dir_NASA = Path('Space_images/Nasa_images')
    path_dir_NASA.mkdir(parents=True, exist_ok=True)
    fetch_nasa_images(url_NASA, api_key_NASA, path_dir_NASA)


if __name__ == "__main__":
    main()
