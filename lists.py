names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[-3])
print(names[2:])
numbers = [3,16,4,8,7]
max = 0
for number in numbers:
    if (number > max):
        max = number
print(f'The largest number in list is: {max}')