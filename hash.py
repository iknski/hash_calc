import hashlib
from os import system
from os.path import basename, dirname, splitext, isfile
from sys import argv
from colorama import init, Fore


init(autoreset=True)


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

# Проверка правильности ввода пути файла
if isfile(argv[2]) is False:
    print("=================================================================")
    print(
        Fore.RED
        + f"Файл {Fore.YELLOW + argv[2] + Fore.RESET}{Fore.RED} не найден. Попробуйте снова!!!"
    )
    print(
        Fore.RED
        + f"File {Fore.YELLOW + argv[2] + Fore.RESET}{Fore.RED} not found. Try again!!!"
    )
    print("=================================================================")
    system("pause")

# Проверка правильности ввода алгоритма хэширования
elif argv[1] not in hashlib.algorithms_available:
    print("=================================================================")
    print(
        Fore.RED
        + f"Неподдерживаемый алгоритм {Fore.YELLOW + argv[1] + Fore.RESET}{Fore.RED}. Попробуйте снова!!!"
    )
    print(
        Fore.RED
        + f"Unsupported hash algorithm {Fore.YELLOW + argv[1] + Fore.RESET}{Fore.RED}. Try again!!!"
    )
    print("-----------------------------------------------------------------")
    print("Поддерживаемые алгоритмы:")
    print("Suported algorithms:")
    print(Fore.GREEN + f"{hashlib.algorithms_available}")
    print("=================================================================")
    system("pause")

else:
    output = hash_file(argv[1], argv[2])

    # Если хэш-файл уже есть, проверить его валидность
    if isfile(f"{path_to_file}\{file_name}.{argv[1]}") is True:
        with open(
            f"{path_to_file}\{file_name}.{argv[1]}", mode="r", encoding="UTF-8"
        ) as hfile:
            line = hfile.readline()
            if line == output:
                print(
                    "================================================================="
                )
                print(
                    f"Файл {Fore.YELLOW + argv[2] + Fore.RESET} проверен.{Fore.GREEN} Хэш сумма совпадает!!!"
                )
                print(
                    f"File {Fore.YELLOW + argv[2] + Fore.RESET} checked.{Fore.GREEN} Hash sum is match!!!"
                )
                print(
                    "================================================================="
                )
                system("pause")
            elif line != output:
                print(
                    "================================================================="
                )
                print(
                    f"Файл {Fore.YELLOW + argv[2] + Fore.RESET} проверен.{Fore.RED} Хэш сумма не совпадает!!!"
                )
                print(
                    f"File {Fore.YELLOW + argv[2] + Fore.RESET} checked.{Fore.RED} Hash sum mismatch!!!"
                )
                print(
                    "================================================================="
                )
                system("pause")

    # Если хэш-файла нет, создать его
    else:
        with open(
            f"{path_to_file}\{file_name}.{argv[1]}", mode="w", encoding="UTF-8"
        ) as hfile:
            hfile.write(output)
        print("=================================================================")
        print(Fore.YELLOW + output)
        print("-----------------------------------------------------------------")
        print(f"Хэш файл сохранен в: {Fore.GREEN}{path_to_file}\{file_name}.{argv[1]}")
        print(f"Hash file saved to: {Fore.GREEN}{path_to_file}\{file_name}.{argv[1]}")
        print("=================================================================")
        system("pause")
