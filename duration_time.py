num_sec=0
while True:

    try:
        str_sec = input('Введите количество секунд или exit: ')
        if str_sec == 'exit':
            break
        else:
            num_sec = int(str_sec)
    except ValueError:
        print('Вы ввели не число')
        continue
    else:
        if num_sec < 60:
            print('Duration: ', num_sec, ' сек')
        elif num_sec < 3600:
            num_min = num_sec // 60
            num_sec = num_sec % 60
            print('Duration: ', num_min, ' мин', num_sec, ' сек')
        elif num_sec < 86400:
            num_hour = num_sec // 3600
            num_min = (num_sec - num_hour * 3600) // 60
            num_sec = num_sec % 60
            print('Duration: ', num_hour, ' час', num_min, ' мин', num_sec, ' сек')
        else:
            num_day = num_sec // 86400
            num_hour = (num_sec - num_day * 86400) // 3600
            num_min = (num_sec - num_day * 86400 - num_hour * 3600) // 60
            num_sec = num_sec % 60
            print('Duration: ', num_day, ' дн', num_hour, ' час', num_min, ' мин', num_sec, ' сек')
