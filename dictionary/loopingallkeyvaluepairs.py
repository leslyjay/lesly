favorite_language = dict(
    Lesly = "Python",
    John = "Java",
    Mary = "C++",
    Alice = "Ruby"
)
for name, language in favorite_language.items():
    print(f"{name}  likes {language}.")
    
# looping through all the keys in a dictionary
for name in favorite_language.keys():
    print(name)
    
friends = ["John","Mary"]
for name in favorite_language.keys():
    print(name)
    if name in friends:
        print("Hi "+ name + ", I see your favorite language is " + favorite_language[name] + "!")
        

for name in sorted(favorite_language.keys()):
    print(name + ", thank you for taking the poll.")