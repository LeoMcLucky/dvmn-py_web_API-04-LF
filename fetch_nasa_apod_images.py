import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from image_utils import get_file_extension, download_img_for_url


def fetch_nasa_images(api_key_nasa, path_dir):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    total_photos = 30
    payload = {
        'api_key': api_key_nasa,
        'count': total_photos,
    }
    response = requests.get(url_nasa, params=payload)
    response.raise_for_status()
    img_urls = response.json()
    for number, img_url in enumerate(img_urls):
        hd_img_url = img_url['hdurl']
        file_ext = get_file_extension(hd_img_url)
        file_name = f'NASA_{number}{file_ext}'
        download_img_for_url(hd_img_url, path_dir, file_name)


def main():
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']
    path_dir_nasa = Path('Space_images/NASA_images')
    path_dir_nasa.mkdir(parents=True, exist_ok=True)
    fetch_nasa_images(api_key_nasa, path_dir_nasa)


if __name__ == "__main__":
    main()
