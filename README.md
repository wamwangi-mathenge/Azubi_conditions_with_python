# Conditions with Python

Your code needs the ability to take different actions based on different conditions

| Symbol | Operation |
| ------ | --------- |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to|
| <= | Less than or equal to |
| == | is equal to |
| != | is not equal to |

Example

```
if price >= 1.00:
    tax = .07
    print(tax)
```

You can add a default action using else

```
if price >= 1.00:
    tax = .07
else:
    tax = 0

print(tax)
```

## String Comparison

String comparison is case sensitive

Example:

```
country = 'CANADA'
if country == 'canada':
    print("You're a Canadian")
else:
    print("You're not from Canada")
```

Output:
```
You're not from Canada
```

Use string functions to make case insensitive comparisons

```
country = "CANADA"
if country.lower() == 'canada':
    print("You're a Canadian")
else:
    print("You're not a Canadian")
```

Output:
```
"You're a Canadian"
```

Conditions allow our code to react to different situations

- Apply appropriate state or federal taxes based on location
- Calculate salary based on job level
- What to do if a file is not found
- What to do if an expected value is missing.

## Complex Conditions

Sometimes you can combine conditions with AND instead of nesting if statements

Example: Requirements for honour roll
- Minimum 85% grade point average
- Lowest grade is at least 70%

```
if gpa >= .85 and lowest_grade >= .70:
    print("Well DOne")
```

## How AND statements are processed

| First Condition | Second Condition | Condition evaluates as |
| --------------- | ---------------- | ---------------------- |
| TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE |
| FALSE | TRUE | FALSE |
| FALSE | FALSE | FALSE |

If you need to remember the results of a condition check later in your code, use Boolean variables as flags

```
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print("Well done")
```

Combining operators allows you to handle complex business rules in your code but must be tested very carefully to avoid introducing errors