weight = float(input('Enter your weight in Kilograms: '))
height = float(input('Enter your height in meters '))
bmi = weight/(height*height)
print('Your BMI is: ', format(bmi, '5.2f'))