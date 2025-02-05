# Using 'with' for reading
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Using 'with' for writing
with open('example2.txt', 'w') as file:
    file.write("This is a new file content.")

# Using 'with' for appending
with open('example2.txt', 'a') as file:
    file.write("\nAppending more content.")
