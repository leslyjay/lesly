num = int(input('Enter a number: '))
numbers=list(range(0,11))
for number in numbers:
    result= num * number
    print(f"{num} x {number} = {result}")