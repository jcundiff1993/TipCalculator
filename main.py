#Intro for the calculator
print("Welcome to the tip calculator!")

#Gains the starting bill amount
bill_amount = float(input("What was the bill? \n"))
print(f"The bill amount is ${bill_amount}.")

#Correctly converts the tip amount to a percentage
tip = float(input("What percent would you like to tip? \n"))
tip_percentage = tip /100
print(f"The tip percentage is {tip_percentage}%.")

#Collects the number of people to split the bill by.
number_of_people = int(input("How many people are splitting the bill? \n"))
print(f"There are {number_of_people} people splitting the bill.")

#Calculates the total bill and rounds to 2 decimal spots.
total_bill = (bill_amount * tip_percentage) + bill_amount
total_bill = round(total_bill, 2)
print(f"The total bill is ${total_bill}.")

#Splits the total bill into an even amount

total_bill_per_person = total_bill / number_of_people
total_bill_per_person = round(total_bill_per_person, 2)
print(f"The total bill per person is ${total_bill_per_person}.")
