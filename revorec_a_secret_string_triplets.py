def change_if_need(letters, a, b):
    if letters.index(a) > letters.index(b):
        letters[letters.index(a)], letters[letters.index(b)] = (
            letters[letters.index(b)],
            letters[letters.index(a)],
        )
    return letters


def recoverSecret(triplets):
    letters = set()
    for i in triplets:
        for j in i:
            letters.add(j)
    letters = list(letters)
    while True:
        flag = letters[::]
        for i in triplets:
            a, b, c = i
            letters = change_if_need(letters, a, b)
            letters = change_if_need(letters, b, c)
            letters = change_if_need(letters, a, c)
        if flag == letters:
            break
    return "".join(letters)


triplets = [
    ["t", "u", "p"],
    ["w", "h", "i"],
    ["t", "s", "u"],
    ["a", "t", "s"],
    ["h", "a", "p"],
    ["t", "i", "s"],
    ["w", "h", "s"],
]

print(recoverSecret(triplets))
