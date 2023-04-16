'''Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию.
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.'''
import os
import json
import csv
import pickle


def content_dir(name_dir: str) -> None:
    with open('content.json', 'w', encoding='utf-8') as f_js, \
            open('cont_dir.csv', 'w', newline='', encoding='utf-8') as f_csv, \
            open('content.dir.pickle', 'wb') as f_picle:
        w = csv.DictWriter(f_csv, fieldnames=['Name', 'Type', 'Parent', 'Size'], dialect='excel-tab',
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        os.chdir(find_dir(name_dir))
        for path_, dir, files, in os.walk(os.getcwd()):
            parent = path_.split('\\')
            parent = parent[-1]
            for directory in dir:
                if dir != []:
                    dic_dir = {}
                    list_dir = []
                    dic_dir['Name'] = directory
                    dic_dir['Type'] = 'DIR'
                    dic_dir['Parent'] = parent
                    list_dir.append(dic_dir)
                    w.writerows(list_dir)
                    json.dump(dic_dir, f_js, ensure_ascii=False, indent=2)
                    pickle.dump(dic_dir, f_picle)
            for fi in files:
                if files != []:
                    dic_files = {}
                    list_files = []
                    file_size = os.path.getsize(f'{path_}/{fi}')
                    dic_files['Name'] = fi
                    dic_files['Type'] = 'FILE'
                    dic_files['Parent'] = parent
                    dic_files['Size'] = f'{file_size} bytes'
                    list_files.append(dic_files)
                    w.writerows(list_files)
                    json.dump(dic_files, f_js, ensure_ascii=False, indent=2)
                    pickle.dump(dic_files, f_picle)
    print(dic_dir)

def find_dir(name_dir: str) -> str:
    os.chdir('\\')
    paths = ''
    desired = ''
    for path_, dirs, files in os.walk(os.getcwd()):
        for i in dirs:
            if i == name_dir:
                paths += f'{path_}\{name_dir};'
    desired = (paths.split(';')[0])
    return desired


if __name__ == '__main__':
    content_dir('For Python')
