class MyErr(Exception):
    pass

a = input('Введите делимое: ')
b = input('Введите делитель: ')

try:
    if int(b) == 0:
        raise MyErr("Деление на ноль запрещено")
    else:
        res = int(a) / int(b)

except ValueError:
    print("Вы ввели не число")
except MyErr as err:
    print(err)
else:
    print(f'Результат деления {a} на {b} = {round(res, 2)}')
finally:
    print("Программа закончена")
