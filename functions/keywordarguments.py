def describe_pet(animal_type,pet_name):
    print("I have a "+animal_type+".")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
describe_pet(animal_type="hamster",pet_name="harry")
describe_pet(pet_name="willie",animal_type="dog")