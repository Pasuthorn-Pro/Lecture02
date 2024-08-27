#คำนวณ BMI
weight = float(input('Enter your weight in Kilograms: '))
height = float(input('Enter your height in meters '))
bmi = weight/(height*height)#สูตรคำนวณหา BMI
print('Your BMI is: ', format(bmi, '.2f'))