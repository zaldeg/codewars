def change_if_need(letters, a, b):
    if letters.index(a) > letters.index(b):
        letters[letters.index(a)], letters[letters.index(b)] = (
            letters[letters.index(b)],
            letters[letters.index(a)],
        )
    return letters


def recoverSecret(triplets):
    r = list(set([i for l in triplets for i in l]))
    print(r)


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
