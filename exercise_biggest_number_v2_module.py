def find_max(numbers):
    maxi = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number
    return maxi
