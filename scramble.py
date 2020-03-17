def make_dict(a):
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


def scramble(s1, s2):
    s1 = make_dict(s1)
    s2 = make_dict(s2)
    for a in s2:
        try:
            if s1[a] < s2[a]:
                return False
        except KeyError:
            return False
    return True


a = "katas"
b = "steak"

print(scramble(a, b))
