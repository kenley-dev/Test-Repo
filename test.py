def isOddOrEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter your number: "))
result = isOddOrEven(num)
print(f"The number {num} is {result}")