def odd_nums(nums):
    for num in range(1, nums + 1, 2):
        yield num


num_input = 15
nums_gen = (num for num in range(1, num_input + 1, 2))
print(type(nums_gen))
print(type(odd_nums(num_input)))

nums_gen_1 = odd_nums(num_input)
print(next(nums_gen_1))
print(next(nums_gen))

print(next(nums_gen_1))
print(next(nums_gen))

print(next(nums_gen_1))
print(next(nums_gen))
