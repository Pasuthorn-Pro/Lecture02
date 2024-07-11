boys = int(input('How many boys in classroom:'))
girls = int(input('How many girls in classroom:'))

total_student = boys+girls

percentage_boys = (boys/total_student)*100
print(f"The percentage is: %", percentage_boys)

percentage_girls = (girls/total_student)*100
print(f"The percentage is: %", percentage_girls)