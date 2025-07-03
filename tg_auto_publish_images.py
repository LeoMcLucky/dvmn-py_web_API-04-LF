import telegram
import random
import time
import argparse
import os
from dotenv import load_dotenv
from pathlib import Path


def parse_input():
    parser = argparse.ArgumentParser(
        description=(
            "Укажите временной отрезок между публикациями фото в секундах"
            "По умолчанию - 14400 секунд = 4 часа."
        )
    )
    parser.add_argument(
        'time_period',
        type=int,
        help='id_spaceX',
        nargs='?',
        default=14400
    )
    args = parser.parse_args()
    return args.time_period


def get_paths_images(path_dir):
    paths_all_images = []
    for dirpath, _, filenames in os.walk(path_dir):
        for filename in filenames:
            if not filename.startswith('.'):
                file_path = Path(dirpath) / filename
                paths_all_images.append(file_path)
    return paths_all_images


def tg_publish_images(tg_bot_token, time_period, path_dir):
    while True:
        paths_images = get_paths_images(path_dir)
        random.shuffle(paths_images)
        for path_image in paths_images:
            bot = telegram.Bot(token=tg_bot_token)
            bot.send_document(chat_id='@NewInterStellar',
                              document=open(path_image, 'rb'))
            time.sleep(time_period)


def main():
    time_period = parse_input()
    load_dotenv()
    tg_bot_token = os.environ['TELEGRAM_TOKEN']
    path_dir = Path('Space_images')
    tg_publish_images(tg_bot_token, time_period, path_dir)


if __name__ == '__main__':
    main()
