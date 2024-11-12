#write a lambda that convert celcius to fahrenheit

celcius_values_list = [0,25,37,78,100]


list_f = map(lambda celsius_value: celsius_value * 9/5 + 32, celcius_values_list)

