import hashlib
from os import system
from os.path import basename, dirname, splitext, isfile
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


file_name = splitext(basename(argv[2]))[0]
path_to_file = splitext(dirname(argv[2]))[0]

if isfile(argv[2]) is False:
    print("========================================")
    print(f'File "{argv[2]}" not found!!! Try again!!!')
    print("========================================")
    system("pause")

elif argv[1] not in hashlib.algorithms_available:
    print("========================================")
    print(f'Unsupported hash algorithm - "{argv[1]}"!!! Try again!!!')
    print("========================================")
    system("pause")

else:
    output = hash_file(argv[1], argv[2])
    if isfile(f"{path_to_file}\{file_name}.{argv[1]}") is True:
        with open(
            f"{path_to_file}\{file_name}.{argv[1]}", mode="r", encoding="UTF-8"
        ) as hfile:
            line = hfile.readline()
            if line == output:
                print("========================================")
                print(f'File "{argv[2]}" checked - hash is match')
                print("========================================")
                system("pause")
            elif line != output:
                print("========================================")
                print(f'File "{argv[2]}" checked - hash is not matched')
                print("========================================")
                system("pause")

    else:
        with open(
            f"{path_to_file}\{file_name}.{argv[1]}", mode="w", encoding="UTF-8"
        ) as hfile:
            hfile.write(output)
        print("========================================")
        print(output)
        print(f"hash file saved: {path_to_file}\{file_name}.{argv[1]}")
        print("========================================")
        system("pause")
