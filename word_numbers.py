
num_range = [2, 3, 4]
for i in range(1,101):
    if (i != 11 and (i % 10) == 1):
        print(i, 'процент')
    elif (i in num_range) or ( i>15 and (i % 10) in num_range):
        print(i, 'процента')
    else:
        print(i, 'процентов')
