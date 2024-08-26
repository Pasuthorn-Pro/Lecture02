boys = int(input('How many boys in classroom:'))#ใส่จำนวนนักเรียนชาย
girls = int(input('How many girls in classroom:'))#ใส่จำนวนนักเรียนหญิง

total_student = boys+girls#หาจำนวนของนักเรียนทั้งห้อง

percentage_boys = (boys/total_student)*100#หาเปอร์เซนของนักเรียนชายต่อนักเรียนทั้งห้อง
print(f"The percentage is: %", percentage_boys)

percentage_girls = (girls/total_student)*100#หาเปอร์เซนของนักเรียนหญิงต่อนักเรียนทั้งห้อง
print(f"The percentage is: %", percentage_girls)