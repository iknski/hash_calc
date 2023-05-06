import hashlib
from os import path
from sys import argv

"""
Подсчет хэшей файла и вывод хэш-суммы в файл.
В качестве первого параметра передать используемый алгоритм.
В качестве второго параметра передать путь к файлу.
Хэш-сумма в виде текстового файла будет лежать рядом с оригинальным файлом.
"""


def hash_file(hashfunc, filepath):
    hash_sum = getattr(hashlib, hashfunc)()
    with open(filepath, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(65536)
            hash_sum.update(chunk)
    return hash_sum.hexdigest()


if __name__ == "__main__":
    file_name = path.splitext(path.basename(argv[2]))[0]
    path_to_file = path.splitext(path.dirname(argv[2]))[0]
    output = hash_file(argv[1], argv[2])

    with open(
        f"{path_to_file}\{file_name}.{argv[1]}", mode="w", encoding="UTF-8"
    ) as hfile:
        hfile.write(output)
