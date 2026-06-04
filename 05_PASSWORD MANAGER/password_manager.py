from cryptography.fernet import Fernet


def load_key():
    with open("key.key", "rb") as file:
        return file.read()


key = load_key()
fer = Fernet(key)


def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" not in data:
                    continue

                user, passw = data.split("|")

                try:
                    decrypted = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted)
                except:
                    print("Could not decrypt one entry (corrupted or wrong key).")

    except FileNotFoundError:
        print("No saved passwords found.")


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Add / View / Q to quit: "
    ).lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
