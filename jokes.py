from random import randint, choice, shuffle, sample

def get_jokes(num, key=True):
    """
    Функция возвращает шутки из трех наборов слов
    :param num: сколько шуток вывести
    :param key: разрешается или запрещаются повторы слов по умолчанию повторы разрешаются
    :return: возвращает заданное количество шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зеленный", "утопичный", "мягкий"]
    jokes = []
    if key:
        for i in range(1, num+1):
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            joky = f'{nouns[0]} {adverbs[0]} {adjectives[0]}'
            jokes.append(joky)
    else:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for i in range(num):
            joky = f'{nouns[i]} {adverbs[i]} {adjectives[i]}'
            jokes.append(joky)

    return print(jokes)

def get_jokes_adv(num, key=True):
    """
    Функция возвращает шутки из трех наборов слов
    :param num: сколько шуток вывести
    :param key: разрешается или запрещаются повторы слов по умолчанию повторы разрешаются
    :return: возвращает заданное количество шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зеленный", "утопичный", "мягкий"]
    jokes = []
    if key: # проверяем можно ли чтоб в шутках повторялись слова
        for i in range(1, num+1):
            shuffle(nouns) # перемешиваем список 1 чтоб не повторялось постояно при вызове функции
            shuffle(adverbs) # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
            shuffle(adjectives) # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
            joky = f'{nouns[0]} {adverbs[0]} {adjectives[0]}' # формируем строку шутки
            jokes.append(joky) # добавляем шутку в список
    else:
        item = 0 # пока шуток 0
        while item < num:
            if item == 0: # если условие верное создаем первую шутку
                joky = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
                jokes.append(joky)
                item += 1
            else:
                keys = True
                joky_str = ' '.join(jokes) # создаем строку из всех шуток списка
                while keys:
                    one_world = choice(nouns) # случайно выбираем первое слово из первого списка
                    two_world = choice(adverbs) # случайно выбираем второе слово из второго списка
                    three_world = choice(adjectives) # случайно выбираем третье слово из третьего списка
                    if (joky_str.find(one_world) != -1) or (joky_str.find(two_world) != -1) or (joky_str.find(three_world) != -1):
                        # проверяем есть ли выбранные слова в существующих шутках
                        keys = True # если есть ничего не делаем и продаолжаем список можно continue
                    else:
                        joky = f'{one_world} {two_world} {three_world}' # если все слова нигде не употреблялись создаем новую шутку
                        jokes.append(joky)
                        keys = False
                        item += 1 # увеличиваем счетчик для создание новой шутки
    return print(jokes)

def get_jokes_adv1(num, key=True):
    """
    Функция возвращает шутки из трех наборов слов
    :param num: сколько шуток вывести
    :param key: разрешается или запрещаются повторы слов по умолчанию повторы разрешаются
    :return: возвращает заданное количество шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зеленный", "утопичный", "мягкий"]
    jokes = []
    if key: # проверяем можно ли чтоб в шутках повторялись слова
        for i in range(1, num+1):
            shuffle(nouns) # перемешиваем список 1 чтоб не повторялось постояно при вызове функции
            shuffle(adverbs) # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
            shuffle(adjectives) # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
            joky = f'{nouns[0]} {adverbs[0]} {adjectives[0]}' # формируем строку шутки
            jokes.append(joky) # добавляем шутку в список
    else:
        shuffle(nouns)  # перемешиваем список 1 чтоб не повторялось постояно при вызове функции
        shuffle(adverbs)  # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
        shuffle(adjectives)  # перемешиваем список 2 чтоб не повторялось постояно при вызове функции
        joky = list(zip(nouns, adverbs, adjectives)) # создаем кортеж из наборов слов в шутках
        for item in joky:
            jokes.append(' '.join(item)) # создаем список из кортежа
    return print(jokes[:num]) # печатаем нужное количество шуток


num_joky = int(input('Сколько шуток вывести: '))
if num_joky <= 4: # при 5 шутках долго работает поиск набора в решении 1 способом
    print(1)
    get_jokes(num_joky)
    print(2)
    get_jokes(num_joky, key=False)
    print(3)
    get_jokes_adv(num_joky)
    print(4)
    get_jokes_adv(num_joky, key=False) # решение первым способом
    print(5)
    get_jokes_adv1(num_joky)
    print(6)
    get_jokes_adv1(num_joky, key=False) # решение вторым способ с помощью zip


else:
    print('None')
