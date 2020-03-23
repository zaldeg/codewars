def primes_numbers(number):
    numbers = set(range(number, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(range(p * p, number + 1, p))
    return primes


def sum_for_list(lst):
    max_abs = max(abs(i) for i in lst)
    primes = primes_numbers(max_abs)
    new_primes = []
    print(primes)
    for i in primes:
        # if [j for j in lst if j % i == 0 and j != i]:
        if [j for j in lst if j % i == 0]:
            new_primes.append(i)
    result = []
    for i in new_primes:
        result.append([i, sum([j for j in lst if j % i == 0])])
    return result


a = [124, -87, -55, -150, -82, 42, -19, -60, -157, -94, 156]
print(sum_for_list(a))
