import os

file_config = 'config.yaml'
if os.path.isfile(file_config):
    with open(file_config, 'r', encoding='utf-8') as f:
        line = f.readline()
        path_config = {}
        while line:
            if line != '':
                len_tab = 0
                while line[len_tab] == ' ':
                    len_tab += 1
                if len_tab == 0:
                    if ':' in line:
                        if not os.path.exists(line.split(':')[0]):
                            os.mkdir(line.split(':')[0])
                            path_config['0'] = line.split(':')[0]
                        else:
                            path_config['0'] = line.split(':')[0]
                    elif '.' in line:
                        with open(line.split(' ')[-1], 'w') as file_crt:
                            file_crt.write(' ')
                elif len_tab > 0:
                    name_is_line = line.lstrip(' ')
                    path_dir = ''
                    range_dir = int(len_tab / 4)
                    for el in range(range_dir):
                        path_dir = f'{path_dir}{path_config[str(el)]}/'
                    if ':' in line:
                        if not os.path.exists(f'{path_dir}{name_is_line.split(":")[0]}'):
                            os.makedirs(f'{path_dir}{name_is_line.split(":")[0]}')
                            path_config[str(range_dir)] = name_is_line.split(":")[0]
                        else:
                            path_config[str(range_dir)] = name_is_line.split(":")[0]
                    elif '.' in line:
                        name_file = (f'{path_dir}{line.split(" ")[-1]}').split('\n')[0]
                        with open(name_file, 'w') as file_crt:
                            file_crt.write(' ')
            line = f.readline()
else:
    print('Нет файла конфигурации')
