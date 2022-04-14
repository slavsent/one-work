class MyErr(Exception):
    pass

num = ''
res_list = []
while num != 'stop':
    num = input('Введите число или stop: ')
    try:
        if num == 'stop':
            break
        elif not num.isdigit():
            raise MyErr("Вы ввели не число")
        else:
            res_list.append(int(num))

    except MyErr as err:
        print(err)

print(res_list)
