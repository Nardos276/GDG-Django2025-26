try:
    with open("config.txt", "w") as file:
        file.write("Nardos Assefa") 
    with open("config.txt") as file:
        name=file.read()
        print(name)
except FileNotFoundError:
    with open("config.txt", "w") as file:
        file.write("Nardos Assefa")
    with open("config.txt") as file:
        name=file.read()
        print("Welcome", name)

