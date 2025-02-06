# Open the file for writing
# file = open('example.txt', 'w')

# Write text to the file
# file.write("Hello, this is a new line.\n")

# Write multiple lines
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# file.writelines(lines)

# Always close the file after writing
# file.close()

# filename = "programming.txt"
# with open(filename, "w") as f_object:
#     f_object.write("I love coding.\n")
#     f_object.write("Programming is interesting.")

filename = "programming.txt"
with open(filename,"a") as f_object:
    f_object.write("\nLearn something new everyday.")