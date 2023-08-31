user_input = input("Give me a word: ")
user_input = user_input.capitalize()
consonant = "a, e, u, o, i"

if user_input[-1] in consonant:
    length = len(user_input)
    user_input += "-inator " + str(length) + "000"
else:
    length = len(user_input)
    user_input += "inator " + str(length) + "000"

print(user_input)