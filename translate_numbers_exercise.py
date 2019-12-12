number_string = input('Phone: ')
numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ''
for number in number_string:
    output += numbers.get(number,"!") + ' '
print(output)


