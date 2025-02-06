print("Enter two numbers and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    try:
        first_number = int(input("Enter the first number: "))
        if first_number == 'q':
            break
        second_number = int(input("Enter the second number: "))
        if second_number == 'q':
            break
        answer = first_number/second_number
    except ZeroDivisionError:
        print("Impossible division.")
    else:
        print(answer)