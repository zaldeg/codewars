def primes(num):
    numbers = set(range(2, num // 2 + 1))
    numbers.difference_update(set(range(4, num // 2 + 1, 2)))
    numbers.difference_update({i for i in range(10, num // 2 + 1) if i % 10 in (5, 0)})
    s = set()
    for i in numbers:
        if [j for j in numbers if i % j == 0 and i != j]:
            s.add(i)
    numbers.difference_update(s)
    return numbers


print(primes(10000))
