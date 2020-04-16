def factors(n):
    if n == 1:
        return [1]
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(n / i)
            factors.append(i)
    return factors


def triangleNum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


factor = []
n = 1
while len(factor) <= 500:
    triangle = triangleNum(n)
    factor = factors(triangle)
    n += 1
print(factor)
print(triangle)
