import requests
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path


def fetch_nasa_epic_images(api_key_nasa, path_dir):
    url_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': api_key_nasa,
    }
    response = requests.get(url_epic, params=payload)
    response.raise_for_status()
    info_photos = response.json()
    for number, info_photo in enumerate(info_photos[:10]):
        img_datetime, img_name = info_photo['date'], info_photo['image']
        img_date = datetime.date.fromisoformat(
            img_datetime.split()[0]).strftime("%Y/%m/%d")
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{img_date}/png/{img_name}.png'
        image_response = requests.get(img_url, params=payload)
        image_response.raise_for_status()
        with open(path_dir / f'EPIC_{number}.png', 'wb') as file:
            file.write(image_response.content)


def main():
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']
    path_dir_epic = Path('Space_images/Nasa_EPIC_images')
    path_dir_epic.mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_images(api_key_nasa, path_dir_epic)


if __name__ == "__main__":
    main()
