temperature = 30

if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

#exercise time
name = input('What is your name? : ')

if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!")