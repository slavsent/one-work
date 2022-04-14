import os
import shutil

dir_name = 'my_project'
if os.path.exists(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.rsplit('.', maxsplit=1)[-1].lower() == 'html':
                list_root = os.path.split(root)
                path_new = os.path.join(f'{dir_name}\\templates\\{list_root[1]}', file)
                path_now = os.path.join(root, file)
                if path_new != path_now:
                    if not os.path.exists(f'{dir_name}/templates/{list_root[1]}'):
                        os.makedirs(f'{dir_name}/templates/{list_root[1]}')
                    shutil.copyfile(path_now, path_new)
else:
    print('Такой директории не существует')
