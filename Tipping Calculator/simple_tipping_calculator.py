#This segment makes use of primitive data types such as strings intergers floats and booleans#

print("Welcome, this is my tipping calculator.")
bill = float(input("What was your total bill?\n"))
tipPercent = int(input("What percentage tip do you desire to give? \nPercentage: "))
groupNum = int(input("If your splitting the bill, among how many people? Type 1 if paying alone.\nPeople: "))
calculation = ((bill + (bill*(tipPercent/100.00))))
costSplit = round(calculation/groupNum, 2)
if(groupNum > 1):
    print(f"Each person should pay: {costSplit:.2f}")
else:
    print(f"The individual should pay: {costSplit:.2f}")