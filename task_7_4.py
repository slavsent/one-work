import os
import json

dir_name = 'some_data'
if os.path.exists(dir_name):
    key_dict_files = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            key_dict_files.append(os.stat(os.path.join(root, file)).st_size)
    max_key = max(key_dict_files)
    i=100
    list_key = [100]
    max_key = max_key//i
    while max_key > 0:
        i *= 10
        list_key.append(str(i))
        max_key = max_key // 10
    dict_num = {}
    dict_ext = {}
    min_key = 0
    for i in list_key:
        dict_num[i] = 0
        dict_ext[i] = []
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if min_key < os.stat(os.path.join(root, file)).st_size <= int(i):
                    dict_num[i] += 1
                    if file.rsplit('.', maxsplit=1)[-1].lower() not in dict_ext[i]:
                        dict_ext[i].append(file.rsplit('.', maxsplit=1)[-1].lower())
        min_key = int(i)
    dict_files = {}
    for i in list_key:
        dict_files[i] = (dict_num[i], dict_ext[i])
    print(dict_files)
    with open(os.path.join(dir_name, f'{dir_name}_summary.json'), 'w') as f:
        json.dump(dict_files, f)

else:
    print('Такой директории не существует')


