celcius = float(input('Enter temperature in celcius:'))

fahrenheit = (celcius * 9/5)+32
print('Temperature in fahrenheit is ',format(fahrenheit, '3.2f'))

kelvin = (celcius + 273.15)
print('Temperature in kelvin is ', format(kelvin, '3.2f'))