# WRITE A FUNCTION OF NUMBERS(A,B) THAT RETURNS THE SUM OF TWO NUMBERS A AND B 
# THEN CALL THE FUNCTION WITH TWO NUMBERS


# print(f"The sum of {first} and {second} is {sum_of_two_numbers}.")

#FIND THE MAXIMUM OF THREE NUMBERS CREATE A FUNCTION MAX_OF_THREE(X,Y,Z) THAT RETURNS THE
# LARGEST OF THREE NUMBERS
# def max_of_three(x,y,z):
#     return max(x,y,z)

# first = int(input("Enter any number: "))
# second = int(input("Enter any number: "))
# third = int(input("Enter any number: "))

# largest = max_of_three(first, second, third)
# print(f"The maximum number among the three is {largest}")

# EVEN OR ODD. WRITE A FUNCTION IS_EVEN(NUMBER) THAT RETURNS TRUE IF NUMBER IS EVEN 
# AND FALSE IF NUMBER IS ODD
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter any number: "))
even = is_even(num)
if even:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")