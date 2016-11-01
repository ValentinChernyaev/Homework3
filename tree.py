# подключаем модуль разбора параметров командной строки
import argparse
# подключаем модуль sys и os
import sys, os

def Print_Tree(walk_dir, folders_only=False,
               include=' ', exclude=' '):

# Обход дерева каталогов
# Прекрасная идея кода с stackoverflow.com
# http://stackoverflow.com/questions/2212643/python-recursive-folder-read
 for root, subdirs, files in os.walk(walk_dir):
    print(root) # вывод каталогов
    if folders_only==False: # вывод и файлов

     for file in files:
          str_file=str(file)
          if include!=" ": # опция печатать ТОЛЬКО найденные с MASK
             if str_file.find(include)!=-1: # нашлось


                print("         "+str_file) # можно подумать насчет
          # увеличивающегося смещения в зависимости от уровня вложения
          if exclude!=" ": # есть опция
             if str_file.find(exclude)==-1: # файла не с  именем MASK

                print("         "+str_file) # печатаем

          if include==" " and exclude==" ": # нет опций выбора файлов

                print("         "+str_file) # печатаем ВСЕ ФАЙЛЫ



 return


# создаём парсер и описываем все параметры командной строки, которые может
# принимать наша программа
parser = argparse.ArgumentParser(
    # начальная строка попомщи по ключу -h (--help)
description='Утилита TREE \
(стилизация под Linux) (версия 1.0), (с) Черняев В.С.',
    # заключительная строка помощи
epilog="Что-то ещё неясно? Обращайтесь к автору.."
)

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'directory',
    # название параметров, которое будет отображено в справке
    metavar='[disk:]\DIRECTORY',
    # сообщаем что ожидается строка
    type=str,
    # параметров будет не меньше одного
    nargs=1,
    # краткое описание параметров
    help='начальный каталог построения'
)

# описываем опцию
# --folders-only
parser.add_argument('-f','--folders_only', action='store_true', default=False,
help='вывод только имён папок')

# описываем взаимоисключающие опции
group = parser.add_mutually_exclusive_group()
# -include
group.add_argument('-i','--include',  nargs=1, metavar='SOME_TEXT', type=str,
default=" ", help='вывод файлов только с вхождением SOME_TEXT')
# и -exclude
group.add_argument('-e','--exclude',  nargs=1, metavar='SOME_TEXT', type=str,
default=' ', help='вывод файлов без  вхождения SOME_TEXT')


# вызываем функцию разбора параметров командной строки
args = parser.parse_args()



# получаем входные значения
start_path = args.directory

if os.path.isdir(start_path[0])==False:
    print("Указанный путь не существует или не является папкой")
    sys.exit(-1)




# Вызов функции печати
if args.include!=" ":
 Print_Tree(start_path[0], folders_only=args.folders_only,
               include=args.include[0])
 sys.exit(0)
if args.exclude!=' ':
 Print_Tree(start_path[0], folders_only=args.folders_only,
                exclude=args.exclude[0])
 sys.exit(0)

Print_Tree(start_path[0], folders_only=args.folders_only)