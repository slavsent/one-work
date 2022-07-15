import requests
from bs4 import BeautifulSoup
import re


def alphabet_animal_dict():
    res = {}
    index_page = 0

    while True:
        if index_page == 0:
            req = requests.get("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")
            index_page = 1
        else:
            req = requests.get(
                f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom={result}")
        html = req.text
        parser = BeautifulSoup(html, "html.parser")
        elements = parser.select("ul")
        list_animals = elements[2].text.split('\n')
        if 'ЖивотныеОрганизмы по алфавиту' != elements[3].text:
            list_animals = list_animals + elements[3].text.split('\n')
        res = list_in_dict(list_animals, res)
        if 'Ящурки' in list_animals:
            break
        else:
            element = list_animals[-1].split()
            result = '+'.join(element)
    return res


def list_in_dict(list_new, res):
    for el in list_new:
        if re.match(r'[А-Я]', el[0]) is not None:
            if el[0] not in res:
                res[el[0]] = 1
            else:
                res[el[0]] = res[el[0]] + 1
    return res


if __name__ == '__main__':
    alphabet_dict = alphabet_animal_dict()
    sorted_tuple = sorted(alphabet_dict.items(), key=lambda x: x[0])
    sort_alphabet_dict = dict(sorted_tuple)
    print(sort_alphabet_dict)
