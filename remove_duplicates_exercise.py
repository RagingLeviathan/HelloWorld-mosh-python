numbers = [1, 4, 6, 8, 8, 8, 86, 13, 31, 45, 7, 6, 7, 4, 5, 9, 23, 45]
print(numbers)
copy = []
for number in numbers:
    if number not in copy:
        copy.append(number)
print(copy)