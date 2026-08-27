# On this code, this is where i learn how to manipulate string 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages: \n\tPython\n\tC\n\tJavaScript")
favorite_language = '   python   '

print(favorite_language.strip())

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)