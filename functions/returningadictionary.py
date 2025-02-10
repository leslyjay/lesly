# def build_person(first_name,last_name):
#     full_name={"first":first_name,"last":last_name}
#     return full_name
# programmer = build_person("lemmy","juma")
# print(programmer)

# optional values
# def build_person(first_name,last_name,age=" "):
#     full_name = {"first":first_name,"last":last_name}
#     if age:
#         full_name ["age"]= age
#     return full_name
# programmer = build_person("lemmy","juma",age=15)
# print(programmer)

# first = int(input("Enter a number: ")) 
# last = int(input("Enter a second number: "))
# a = first
# b = last
# def sum_numbers(a,b):
#     total = a + b
#     return(total)
# result = sum_numbers(first,last)
# print(result)
# print(f"{a} + {b} = {result}")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
w = first
y = second
z = third
def max_of_three(w,y,z):
    list_numbers = [first,second,third]
    max(list_numbers)
    return max
largest = max_of_three(first, second, third)
print(largest)