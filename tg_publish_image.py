import telegram
import random
import argparse
import os
from dotenv import load_dotenv
from pathlib import Path
from image_utils import get_paths_images


def parse_input():
    parser = argparse.ArgumentParser(
        description=(
            "Эта программа публикует в указанном телеграм канале выбранную фотографию по её пути.\n"
            "Если путь не указан, то публикует рандомную фотографию из директория программы.\n\n"
            "Примеры использования:\n"
            "python tg_publish_image.py\n"
            "python tg_publish_image.py 'Space_images/you_image.png'\n"
        ),
        epilog=(
            "Для работы требуется .env файл:\n."
            "TELEGRAM_TOKEN=your_bot_token_here\n"
            "А также 'chat_id' канала или чата указывается прямо в коде или добавляется в .env."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'img_path',
        help="Путь к изображению (если не указан — выберется рандомная фотография)",
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
