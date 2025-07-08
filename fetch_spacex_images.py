import requests
import argparse
from pathlib import Path
from images_utils import get_file_extension, download_img_for_url


def parse_input():
    parser = argparse.ArgumentParser(
        description=(
            "Эта программа скачивает фотографии запуска ракет с помощью API SpaceX.\n"
            "Если ID запуска не указан, то используется крайний запуск ('latest').\n\n"
            "Примеры использования:\n"
            "python fetch_spacex_images.py\n"
            "python fetch_spacex_images.py 5eb87d2dffd86e000604b376\n"
        ),
        epilog="Фотографии сохраняются в директорий 'Space_images/SpaceX_images'.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'id_spaceX',
        help="ID запуска ракеты (по умолчанию: 'latest')",
        nargs='?',
        default='latest'
    )
    args = parser.parse_args()
    return args.id_spaceX


def fetch_spacex_launch(url_spaceX, path_dir):
    response = requests.get(url_spaceX)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    for number, image_url in enumerate(images_urls):
        file_ext = get_file_extension(image_url)
        file_name = f'spaceX_{number}{file_ext}'
        download_img_for_url(image_url, path_dir, file_name)


def main():
    id_spaceX = parse_input()
    url_spaceX = f'https://api.spacexdata.com/v5/launches/{id_spaceX}'
    path_dir_spaceX = Path('Space_images/SpaceX_images')
    path_dir_spaceX.mkdir(parents=True, exist_ok=True)
    fetch_spacex_launch(url_spaceX, path_dir_spaceX)


if __name__ == "__main__":
    main()
