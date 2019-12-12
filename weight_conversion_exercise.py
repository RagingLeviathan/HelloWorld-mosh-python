weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'l':
    weight_in_kg = weight * 0.45
    print(f"You are {weight_in_kg} kilograms.")
elif unit.lower() == 'k':
    weight_in_pounds = weight / 0.45
    print(f"You are {weight_in_pounds} pounds.")