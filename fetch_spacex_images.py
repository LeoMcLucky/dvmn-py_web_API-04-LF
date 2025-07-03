import requests
import argparse
from pathlib import Path
from get_file_data import get_file_extension


def parse_input():
    parser = argparse.ArgumentParser(
        description=(
            "ID запуска SpaceX"
            "По умолчанию 'latest' - (крайний запуск)"
        )
    )
    parser.add_argument(
        'url',
        help='id_spaceX',
        nargs='?',
        default='latest'
    )
    args = parser.parse_args()
    return args.url


def fetch_spacex_launch(url_spaceX, path_dir):
    response = requests.get(url_spaceX)
    response.raise_for_status()
    list_url_images = response.json()['links']['flickr']['original']
    for number, url_image in enumerate(list_url_images):
        file_ext = get_file_extension(url_image)
        image_response = requests.get(url_image)
        image_response.raise_for_status()
        with open(path_dir / f'spaceX_{number}{file_ext}', 'wb') as file:
            file.write(image_response.content)


def main():
    id_spaceX = parse_input()
    url_spaceX = f'https://api.spacexdata.com/v5/launches/{id_spaceX}'
    path_dir_scapeX = Path('Space_images/SpaceX_images')
    path_dir_scapeX.mkdir(parents=True, exist_ok=True)
    fetch_spacex_launch(url_spaceX, path_dir_scapeX)


if __name__ == "__main__":
    main()
