def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
artist = get_formatted_name("future","hendricks")
print(artist)

# making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

artist_with_middle = get_formatted_name("future", "hendricks", " ")
print(artist_with_middle)