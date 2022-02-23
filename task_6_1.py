with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1og:
    list_datas = []
    line = file_1og.readline()
    spamer = {}
    while line:
        list_data = line.split()
        datas = (list_data[0], list_data[5].split('"')[1], list_data[6])
        list_datas.append(datas)
        if list_data[0] in spamer:
            spamer[list_data[0]] += 1
        else:
            spamer[list_data[0]] = 1
        line = file_1og.readline()
print(list_datas[:4])
num_req = max(spamer.values())
spam_ip = [key for key, val in spamer.items() if val == num_req]
print(f'Спамер {spam_ip[0]} сделал запросов: {num_req}')
