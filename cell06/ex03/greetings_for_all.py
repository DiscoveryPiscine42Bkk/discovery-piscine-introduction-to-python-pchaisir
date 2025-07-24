def greetings(name="stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error: Input was not a name.")

greetings("Alexandra")
greetings()
greetings(42)
