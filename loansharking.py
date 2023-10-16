# trying to make a loan calculator

interest = 10
amount = float(input("Enter amount you'd like to borrow: "))
years = int(input("Enter the number of years you'd like to borrow it for: "))
annualInterest = amount * interest / 100
total = (annualInterest * years) + amount
monthlyPayment = total / (years * 12)
print("Your monthly payment equates to", monthlyPayment)

# "savings plan"

import time
import datetime

pay_in = float(input("Enter amount you'd like to deposit: "))
currentyear = 2023

def timecheck():
	while currentyear == 2023:
		timecheck()
	if currentyear != 2023:
		pay_in = pay_in * 2
		pay_in = pay_in * 1.1
		currentyear = currentyear + 1
		time.sleep(31536000)
		d1 = datetime.datetime.strptime('31/12/2023', "%d/%m/%Y").date()
		d2 = datetime.datetime.strptime('14/09/2023', "%d/%m/%Y").date()
		d2>d1

		# uiqaewcdyhrtgbujeb3hy3quwttttteuihjdfcuibvcd