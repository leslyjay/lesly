# WRITE A PROGRAM TAHT ASKS THE USER FOR THEIR AGE AND CHECKS 
# IF THE AGE IS LSS THAN 18 PRINT YOU ARE A MINOR IF THE AGE IS BETWEEN 18 AND 60
# PRINT YOU ARE AN ADULT ELSE PRINT YOU ARE A SENIOR CITIZEN
def age_group(age):
    if age < 18:
        return "You are a minor."
    elif age >= 18 and age <= 60:
        return "You are an adult."
    else:
        return "You are a senior citizen."
age = int(input("Enter your age: "))
group = age_group(age)
agee = group
print(agee)


# SUM OF EVEN NUMBERS:
# WRITE A PROGRAM THAT CALCULATES THE SUM OF ALL EVEN NUMBERS BETWEEN 1 AND 100 USING A FOR LOOP
# def sum_of_even_numbers():
#     total = 0
#     for number in range(1,101):
#         if number % 2 == 0:
#             total += number
#     return total
# sum_even = sum_of_even_numbers()
# print(f"The sum of all even numbers between 1 and 100 is {sum_even}.")  