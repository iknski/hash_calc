import hashlib
from os import system
from os.path import basename, dirname, splitdrive, splitext, isfile
from sys import argv
from rich import box
from rich.console import Console
from rich.table import Table


console = Console()


def hash_file(hashfunc, filepath):
    hash_sum = getattr(hashlib, hashfunc)()
    with open(filepath, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(65536)
            hash_sum.update(chunk)
    return hash_sum.hexdigest()


file_name = splitext(basename(argv[2]))[0]
path_to_file = str()
for _ in splitdrive(dirname(argv[2])):
    path_to_file += _

# Проверка правильности ввода пути файла
if isfile(argv[2]) is False:
    console.print(
        f"+--------------------------------------------------------------------+\n"
        f"Файл * [u][yellow]{argv[2]}[/yellow][/u] * не найден. Попробуйте снова!!!\n"
        f"File * [u][yellow]{argv[2]}[/yellow][/u] * not found. Try again!!!\n"
        f"+--------------------------------------------------------------------+",
        style="red")
    system("pause")

# Проверка правильности ввода алгоритма хэширования
elif argv[1] not in hashlib.algorithms_available:
    hash_algs = ", ".join(list(hashlib.algorithms_available))
    console.print(
        f"+--------------------------------------------------------------------+\n"
        f"Неподдерживаемый алгоритм * [yellow]{argv[1]}[/yellow] *. Попробуйте снова!!!\n"
        f"Unsupported hash algorithm * [yellow]{argv[1]}[/yellow] *. Try again!!!\n"
        f"+--------------------------------------------------------------------+",
    style="red")

    # табличный вывод
    table = Table(box=box.ASCII2,header_style="green", style="green", width=70)
    table.add_column(f"Поддерживаемые алгоритмы\nSuported algorithms", justify="center", style="blue", no_wrap=False)
    table.add_row(f"{hash_algs}")
    console.print(table)
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
                console.print(
                    f"+--------------------------------------------------------------------+\n"
                    f"Файл * [yellow]{argv[2]}[/yellow] * проверен. Хэш сумма совпадает!!!\n"
                    f"File * [yellow]{argv[2]}[/yellow] * checked. Hash sum is match!!!\n"
                    f"+--------------------------------------------------------------------+",
                style="green")
                system("pause")

            elif line != output:
                console.print(
                    f"+--------------------------------------------------------------------+\n"
                    f"Файл * [yellow]{argv[2]}[/yellow] * проверен. Хэш сумма не совпадает!!!\n"
                    f"File * [yellow]{argv[2]}[/yellow] * checked. Hash sum mismatch!!!\n"
                    f"+--------------------------------------------------------------------+",
                style="red")
                system("pause")

    # Если хэш-файла нет, создать его
    else:
        with open(f"{path_to_file}\{file_name}.{argv[1]}", mode="w", encoding="UTF-8") as hfile:
            hfile.write(output)
        table = Table(box=box.ASCII2,header_style="green", style="green", width=70)
        table.add_column(f"{argv[1]}sum", justify="center", style="blue", no_wrap=False)
        table.add_row(f"{output}")
        console.print(table)
        console.print(
            f"Хэш файл сохранен в: * [u][yellow]{path_to_file}\{file_name}.{argv[1]}[/yellow][/u] *\n"
            f"Hash file saved to: * [u][yellow]{path_to_file}\{file_name}.{argv[1]}[/yellow][/u] *\n"
            f"+--------------------------------------------------------------------+",
            style="green")
        system("pause")
