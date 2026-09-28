def get_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Invalid input. Please enter a number!")

def get_str(msg):
    while True:
        inp = input(msg).strip()
        if inp == "":
            print("This cannot be blank. Try again.")
        else:
            return inp