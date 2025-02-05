def build_person(first_name,last_name):
    full_name={"first":first_name,"last":last_name}
    return full_name
programmer = build_person("lemmy","juma")
print(programmer)

# optional values
def build_person(first_name,last_name,age=" "):
    full_name = {"first":first_name,"last":last_name}
    if age:
        full_name ["age"]= age
    return full_name
programmer = build_person("lemmy","juma")
print(programmer)