import requests
import datetime


def currency_rates(currency):
    '''
    Функция возвращает курс валюты к рублю по наименованию валюты к примеру usd
    :param currency: наименования курса валюты
    :return: курс введенной вылюты к рублю на текущее число
    '''
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code == 200:
        content_text = response.text
        data = datetime.datetime.strptime(content_text.split('Date=')[1].split('"')[1], '%d.%m.%Y')
        print(data, type(data))
        if currency.upper() in content_text:
            content_text_cur = content_text.split(currency.upper())[1]
            name_cur = content_text_cur.split('Name>')[1].split('<')[0]
            fig_cur = float(content_text_cur.split('<Value>')[1].split('<')[0].replace(',', '.'))
            print(fig_cur, type(fig_cur))
            print(f'Курс рубля на {data:%d.%m.%y} к валюте {name_cur} {currency.upper()} сщставляет: {fig_cur:.4f}')
        else:
            return print('Такой валюты нет')
    else:
        return print('Not Found.')


if __name__ == '__main__':
    currencys = input('Введите код валюты: ')
    currency_rates(currencys)
