#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = bill * (1 + percentage/100)

number_of_people = int(input("How many people to split the bill? "))
bill_per_persone = round(total_bill / number_of_people , 2)
bill_per_persone = "{:.2f}".format(bill_per_persone) #to show the zeros at the end of a float

print(f"Each persone should pay: ${bill_per_persone}")
