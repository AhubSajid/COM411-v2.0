print("Enter first number")
input1 = int(input())
print("Enter second number")
input2 = int(input())
print("Enter third number")
input3 = int(input())

oddcount = 0
evencount = 0

if input1 % 2 == 1:
    oddcount += 1
else:
    evencount += 1

if input2 % 2 == 1:
    oddcount += 1
else:
    evencount += 1

if input3 % 2 == 1:
    oddcount += 1
else:
    evencount += 1

print(f"There were",oddcount,"odd numbers and ",evencount,"even numbers")