cube_num = []
for i in range (1, 1001):
    if (i % 2) > 0:
        cube_num.append(i**3)
sum_num_7 = 0
sum_num_7_17 = 0
for num in cube_num:
    sum_fig = 0
    sum_fig_17 = 0
    for fig in str (num):
        sum_fig += int (fig)
    if (sum_fig % 7) == 0:
        sum_num_7 += num
    for fig in str (num+17):
        sum_fig_17 += int (fig)
    if (sum_fig_17 % 7) == 0:
        sum_num_7_17 += num + 17
# print (cube_num)
print('Сумма чисел, сумма цифр, которых делится на 7: ', sum_num_7)
print('Сумма чисел с увеличением на 17, сумма цифр, которых делится на 7: ', sum_num_7_17)

