list_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list_data):
    if list_data[i].isdigit() or list_data[i].strip('+').isdigit() or list_data[i].strip('-').isdigit():
        if int(list_data[i]) < 10 and int(list_data[i]) > -10:
            if list_data[i].find('+') != -1:
                list_data[i] = '+0' + str(int(list_data[i]))
            elif list_data[i].find('-') != -1 :
                list_data[i] = '-0' + str(-int(list_data[i]))
            else:
                list_data[i] = '0' + list_data[i]
        list_data.insert(i, '"')
        list_data.insert(i+2,'"')
        i += 3
    else:
        i += 1

list_str = ''
for i, data in enumerate(list_data):
    if (data == '"' and list_data[i+1].isdigit()) or (data.isdigit()) or (data.find('+') != -1) or \
            (data.find('-') != -1) or (data == '"' and list_data[i+1].find('-') != -1) \
            or (data == '"' and list_data[i+1].find('+') != -1):
        list_str += data
    else:
        list_str = list_str + data + ' '


print(list_str)


print(list_data)

