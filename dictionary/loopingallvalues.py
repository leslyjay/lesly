# looping through all values in a dictionary
favorite_language = dict(
    Lesly = "Python",
    John = "Java",
    Mary = "C++",
    Alice = "Ruby"
)
print("The following languages have been mentioned: ")
for language in favorite_language.values():
    print(language)

print("The following languages have been mentioned: ")    
for language in set(favorite_language.values()):
    print(language)