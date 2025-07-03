import telegram
import random
import argparse
import os
from dotenv import load_dotenv
from pathlib import Path
from get_file_data import get_paths_images


def parse_input():
    parser = argparse.ArgumentParser(
        description=(
            "Укажите путь желаемой фотографий"
            "По умолчанию - случайная фотография"
        )
    )
    parser.add_argument(
        'img_path',
        help='id_spaceX',
        nargs='?',
        default=''
    )
    args = parser.parse_args()
    return args.img_path


def tg_publish_image(tg_bot_token, img_path, path_dir):
    if not img_path:
        paths_images = get_paths_images(path_dir)
        path_image = random.choice(paths_images)
    else:
        path_image = img_path

    bot = telegram.Bot(token=tg_bot_token)
    bot.send_document(chat_id='@NewInterStellar',
                      document=open(path_image, 'rb'))


def main():
    img_path = parse_input()
    load_dotenv()
    tg_bot_token = os.environ['TELEGRAM_TOKEN']
    path_dir = Path('Space_images')
    tg_publish_image(tg_bot_token, img_path, path_dir)


if __name__ == '__main__':
    main()
