def isPrime(n, prime_array):
    for i in prime_array:
        if n % i == 0:
            return False
    return True

prime_array = [2]
i = 2
while len(prime_array) < 10001:
    if isPrime(i, prime_array):
        prime_array.append(i)
    i += 1
print(prime_array[-2])
