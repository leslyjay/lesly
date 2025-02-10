# FUNCTION FOR FACTORIAL CALCULATION: WRITE A FUNCTION FACTORIAL(N) THAT CALCULATES THE FACTORIAL
# (N!) OF A GIVEN NUMBER N. USE A  FOR LOOP AND IF STATEMENT TO HANDLE THE CASE OF 0
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         fact = 1
#         for number in range(1,n+1):
#             fact *= number
#         return fact
# num = int(input("Enter any number: "))
# fact = factorial(num)
# print(f"The factorial of {num} is {fact}.")

# PRIME NUMBER CHECKER: WRITE A FUNCTION IS_PRIME(NUMBER) THAT CHECKS WHETHER A NUMBER IS PRIME. 
# USE A LOOP AND CONTROL FLOW TO  CHECK DIVISIBILITY AND RETURN TRUE IF THE NUMBER IS PRIME 
# OTHERWISE RETURN FALSE
def is_prime(number):
    if number < 2:
        return False
    for num in range(2,number):
        if number % num == 0:
            return False
    return True
num = int(input("Enter any number: "))
prime = is_prime(num)
if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")