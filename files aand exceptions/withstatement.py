# Using 'with' for reading
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Using 'with' for writing
# with open('example2.txt', 'w') as file:
#     file.write("This is a new file content.")

# Using 'with' for appending
# with open('example2.txt', 'a') as file:
#     file.write("\nAppending more content.")
    
# filename = "example.txt"
# with open(filename) as f_obj:
#     lines = f_obj.readlines()
# for line in lines:
#     print(line.rstrip())
    
filename = "example.txt"
with open(filename) as f_object:
    lines = f_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
print(pi_string[:54] + "...")