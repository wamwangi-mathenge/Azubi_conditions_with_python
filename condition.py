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