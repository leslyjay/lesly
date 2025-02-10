# WRITE A PROGRAM THAT PRINTS NUMBERS FROM 1 TO 30 BUT FOR MULTIPLES OF 3 PRINT FIZZ. FOR MULTIPLES
# OF 5 PRINT BUZZ AND FOR MULTIPLES OF BOTH 3 AND 5 PRINT FIZZBUZZ
def fizzbuzz():
    for number in range(1,31):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizzbuzz()