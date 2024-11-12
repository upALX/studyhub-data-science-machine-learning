#write a lambda that convert celcius to fahrenheit

celcius_values_list = [0,25,37,78,100]


list_f = map(lambda celsius_value: celsius_value * 9/5 + 32, celcius_values_list)


#use function not lambda to read an list and return a new list with a multiple of 3 of each value inside the list

list_values = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def get_multiple_3(list_multiple_values: list) -> list:
    multiples_3_list = [value for value in list_multiple_values if value % 3 == 0]

    return multiples_3_list

list_multiple_3 = get_multiple_3(list_multiple_values=list_values)

print(list_multiple_3)

# get a list of numbers and  use map and lambda to get the pow of each value on the list

values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqrt_list = list(map(lambda value: value ** 2, values_list))
print(sqrt_list)


