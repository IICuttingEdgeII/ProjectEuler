import math
import time


# method 1
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def method1():
    t0 = time.time()
    total = 0

    for n in range(1, 2000000):
        if is_prime(n):
            total += n
    print("Total of primes:", total)

    t1 = time.time()
    print("Time required :", t1 - t0)


# method 2

def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is
        # a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    total = 0

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            total += p
    return total


def method2():
    t0 = time.time()
    c = SieveOfEratosthenes(200000000)
    print("Total prime numbers in range:", c)

    t1 = time.time()
    print("Time required:", t1 - t0)
method2()