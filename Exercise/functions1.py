# AREA OF  A CIRCLE. WRITE A FUNCTION AREA_OF_CIRCLE(RADIUS) THAT RETURNS THE AREA OF A CIRCLE
def area_of_circle(radius):
    area = 3.142 * radius ** 2
    return area
r = float(input("Enter the radius of the circle: "))
calculation = area_of_circle(r)
print(F"For a circle of {r} in radius, it's area is {calculation}. ")

# WRITE A FUNCTION IS_PALINDROME(WORD) THAT CHECKS IF A GIVEN STRING IS A PALINDROME. IT SHOULD
# RETURN