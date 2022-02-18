src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

repeat_num = set()
result = set()
for num in src:
    if num in repeat_num:
        continue
    if num in result:
        repeat_num.add(num)
        result.discard(num)
        continue
    result.add(num)

print(result)
print([el for el in src if el in result])
