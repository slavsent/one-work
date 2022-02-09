data_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for data in data_list:
    name = data.split()[-1].capitalize()
    print(f'Привет {name}!')
