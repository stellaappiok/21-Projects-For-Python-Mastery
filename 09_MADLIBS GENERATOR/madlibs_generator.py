with open("story.txt", "r") as file:
    text = file.read()

placeholders = []
current_word = ""
inside_placeholder = False

for character in text:
    if character == "<":
        inside_placeholder = True
        current_word = "<"

    elif character == ">" and inside_placeholder:
        current_word += ">"
        if current_word not in placeholders:
            placeholders.append(current_word)
        inside_placeholder = False

    elif inside_placeholder:
        current_word += character

user_words = {}

for placeholder in placeholders:
    replacement = input(f"Enter a word for {placeholder}: ")
    user_words[placeholder] = replacement

for placeholder, replacement in user_words.items():
    text = text.replace(placeholder, replacement)

print("\nGenerated Story:\n")
print(text)
