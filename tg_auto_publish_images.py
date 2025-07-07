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
            "Эта программа публикует в указанном телеграм канале рандомную фотографию, из указанной директории.\n"
            "Публикация осуществляется через равные установленные промежутки времени или по умолчанию каждые 4 часа.\n\n"
            "Примеры использования:\n"
            "python tg_auto_publish_images.py\n"
            "python tg_auto_publish_images.py 3\n"
        ),
        epilog=(
            "Для работы требуется .env файл:\n."
            "TELEGRAM_BOT_TOKEN=your_bot_token_here\n"
            "А также 'chat_id' канала или чата указывается прямо в коде или добавляется в .env."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'time_period',
        type=int,
        help="Временной период в секундах (если не указан — по умолчанию используется '14400' секуны (4 часа)",
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
    tg_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    path_dir = Path('Space_images')
    tg_publish_images(tg_bot_token, time_period, path_dir)


if __name__ == '__main__':
    main()
