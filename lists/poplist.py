motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle.title())
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.

# The last motorcycle I owned was a Suzuki.
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')