# If-else statement

price = input("How much did you pay? ")
price = float(price)

if price >= 1.00:
    tax = 0.07
else:
    tax = 0
    
print(f"Tax rate is: {tax}")

# String Comparison

country = "KENYA"

if country == "kenya":
    print("You're a Kenyan")
else:
    print("You're not a Kenyan")
    

# Using string functions to make case insensitive comparisons

if country.lower() == 'kenya':
    print("You're a Kenyan")
else:
    print("You're not a Kenyan")
    
    

# A student makes honour roll if the average is >=85
# and their lowest grade is not below 75

gpa = float(input("What was your GPA? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .75:
    honour_roll = True
else:
    honour_roll = False
    
if honour_roll:
    print("You made the honour roll")
else:
    print("You did not make the honour roll")