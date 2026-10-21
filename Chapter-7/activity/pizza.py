prompt = "Enter pizzas\n"
prompt += "Type 'quit' to send: "


while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print(f"You add {pizza.title()} to your pizza\n")