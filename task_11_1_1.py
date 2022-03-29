class Date:
    date_day = 0
    date_month = 0
    date_year = 0

    def __init__(self, date_str):
        self.date_str = date_str
        Date.set_date(self.date_str)

    def __str__(self):
        return Date.valid_date(self.date_day, self.date_month, self.date_year)

    @classmethod
    def set_date(cls, date_str):
        list_date = date_str.split('-')
        if len(list_date) == 3:
            str_day, str_month, str_year = list_date
        else:
            return "Неверный формат даты"
        try:
            cls.date_day = int(str_day)
            cls.date_month = int(str_month)
            cls.date_year = int(str_year)
            return cls.valid_date(cls.date_day, cls.date_month, cls.date_year)
        except ValueError as err:
            return "Неверный формат даты"

    @staticmethod
    def valid_date(date_day, date_month, date_year):
        date_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
                     '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
        # нулевые даты не бируться так как в реальной ситуации не имеют смысла
        if date_year <= 0:
            return "Год не может быть отрицательным и 0"
        elif not (0 <= date_month <= 12):
            return "Месяц может быть от 1 до 12"
        elif not (0 <= date_day <= 31):
            return "День может быть от 1 до 31"
        elif date_month == 2 and date_day > 29 and (date_year % 4 == 0):
            return "В високосном году в феврале не может быть больше 29 дней"
        elif (date_month == 2 and date_day > 28 and (date_year % 4 != 0)) or (
                date_day > date_dict[str(date_month)] and date_month != 2):
            return f"В месяце {date_month} не может быть дней {date_day}"
        else:
            return f'{date_day} {date_month} {date_year}'


date_1 = Date('30-6-2020')
print(date_1)
print(date_1.set_date('29-2-2020'))
