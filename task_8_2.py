import re


def parsing_log(file_name):
    with open(file_name, encoding='utf-8') as file_1og:
        parsing_list = []
        line = file_1og.readline()
        while line:
            pattern_1 = re.compile(r'^[a-z,0-9,:,.]*')
            pattern_2 = re.compile(r'\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}\s+[+]\d{4}')
            pattern_3 = re.compile(r'"([^"]+)\s(/\w+/\w+)')
            params_34 = pattern_3.finditer(line)
            for item in params_34:
                param_3 = item.group(1)
                param_4 = item.group(2)
            pattern_4 = re.compile(r'(\d{3})\s([0-9]*)\s')
            params_56 = pattern_4.finditer(line)
            for item in params_56:
                param_5 = item.group(1)
                param_6 = item.group(2)
            data = (pattern_1.findall(line)[0], pattern_2.findall(line)[0], param_3, param_4, param_5, param_6)
            parsing_list.append(data)
            line = file_1og.readline()
    return parsing_list


if __name__ == '__main__':
    print(parsing_log('nginx_logs.txt'))
