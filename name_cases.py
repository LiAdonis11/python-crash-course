# i also practice how to manipulate string here
name = "Gors gorio"
question = "are you having fun?"
full_message = f'{name}, {question}'
print(full_message)
print(name.lower())
print(name.upper())
print(name.title())

quote = 'once said, "Success is not final, failure is not fatal: it is the courage to continue that counts"'
famous_name = "Winston Churchill"
message = f"{famous_name} {quote}"
print(message)

richest_man = "\tElon \n\tMask"
print(richest_man)
print(richest_man.lstrip())
print(richest_man.rstrip())
print(richest_man.strip())

filename = "python_notes.txt"
print(filename.removesuffix('.txt'))