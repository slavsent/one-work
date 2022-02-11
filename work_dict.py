def num_translate(world_eng):
    """
    Функция получает в качестве аргумента слово на английском языке от 1 до 10
    например one, функция возвращает перевод этого слова на русский язык
    если такого числа нет то выведится None
    """
    dict_eng = {
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five' : 'пять',
        'six' : 'шесть',
        'seven' : 'семь',
        'eight' : 'восемь',
        'nine' : 'девять',
        'ten' : 'десять',
    }
    if world_eng in dict_eng:
        return print(dict_eng[world_eng])
    else:
        return print('None')


def num_translate_adv(world_eng):
    """
    Функция получает в качестве аргумента слово на английском языке от 1 до 10
    например one, функция возвращает перевод этого слова на русский язык
    если такого числа нет то выведится None
    В качестве дополнения если введенная цифра с большой буквы то и русский перевод будет с большой буквы
    """
    dict_eng = {
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five' : 'пять',
        'six' : 'шесть',
        'seven' : 'семь',
        'eight' : 'восемь',
        'nine' : 'девять',
        'ten' : 'десять',
    }
    if world_eng.lower() in dict_eng:
        if world_eng.istitle():
            return print(dict_eng[world_eng.lower()].title())
        else:
            return print(dict_eng[world_eng.lower()])
    else:
        return print('None')

world_num = input('Введите число от 1 до 10 на английском языке: ')
num_translate(world_num)

world_num_adv = input('Введите число от 1 до 10 на английском языке: ')
num_translate_adv(world_num_adv)