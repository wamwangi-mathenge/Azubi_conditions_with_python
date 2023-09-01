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