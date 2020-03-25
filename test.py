def power(a, n):
    if n == 2:
        return a * a
    if n % 2 == 0:
        return power(a, n / 2) * power(a, n / 2)
    if n == 1:
        return a
    if n % 2 == 1:
        return a * power(a, (n - 1) / 2) * power(a, (n - 1) / 2)


a = 2
n = 3
print(power(2, 10))
