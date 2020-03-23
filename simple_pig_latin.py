def pig_it(text):
    text = text.split()
    for i, word in enumerate(text):
        if word.isalpha():
            text[i] = word[1 : len(word)] + word[0] + "ay"
    return " ".join(text)


print(pig_it("Hello world !"))
