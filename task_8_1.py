import re


def email_parse(email_name):
    pattern_valid = re.compile(r'[@]')
    pattern_valid_s = re.compile(r'\s')
    pattern_valid_point = re.compile(r'\.')

    if pattern_valid.search(email_name) != None and pattern_valid_s.search(
            email_name) == None and pattern_valid_point.search(email_name) != None:
        dict_email_name = {}
        pattern = re.compile(r'[@]')
        if pattern_valid_point.search(pattern.split(email_name)[1]) != None:
            dict_email_name['username'] = pattern.split(email_name)[0]
            dict_email_name['domain'] = pattern.split(email_name)[1]
            return dict_email_name
        else:
            raise ValueError('Ошибка в написании адреса e-mail')
    else:
        raise ValueError('Ошибка в написании адреса e-mail')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    # print(email_parse('someone_geekbrains.ru'))
    # print(email_parse('someon e@geekbrains.ru'))
    # print(email_parse('someone@geekbrainsru'))
