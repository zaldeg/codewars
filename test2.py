import math


def sum_for_list(lst):
    num = max([abs(i) for i in lst])
    set_of_primes = set()
    for i in range(2, int(math.sqrt(num) + 1)):
        if [j for j in range(2, i // 2 + 1) if i % j == 0] == []:
            set_of_primes.add(i)
    a = []
    for prime in set_of_primes:
        for number in lst:
            if number % prime == 0 and prime not in a and prime != number:
                a.append(prime)
    return [[i, sum(j for j in lst if j % i == 0)] for i in sorted(a)]


i = [12, 15]
print(sum_for_list(i))
