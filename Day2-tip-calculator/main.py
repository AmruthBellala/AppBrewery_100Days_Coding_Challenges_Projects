#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to tip calculator")
Bill_amt = eval(input("What was the total bill?$ "))
Tip_amt = eval(input("What percentage tip would you like to give? 10,12 or 15? "))
persons = eval(input("How many people to split the bill? "))

percent = Bill_amt * Tip_amt/100

New_Bill = Bill_amt + percent

Total_bill = (New_Bill / persons)
print(f"Each person should pay ${round(Total_bill,2)}")