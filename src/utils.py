import json
import gzip
import shutil
from typing import Dict, Any, List


def read_json(path: str) -> Dict:
    """
    Функция чтения JSON файла
    :param path: путь до файла
    :return: объект JSON
    """
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        return data


def compression_file(path: str) -> None:
    """
    Функция сжимает файл JSON
    :param path: путь до файла
    :return: ничего
    """
    with open(path, 'rb') as f_in:
        with gzip.open(f'{path}.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
