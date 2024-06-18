result = numbers[0]
for num in numbers:
        if result > num:
            result = num
min_number = get_min_numbers(numbers)
print("Min number: ", min_number)