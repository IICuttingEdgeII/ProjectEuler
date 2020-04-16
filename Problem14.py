# Collatz Sequence
import time


# shitty recursive solution, not optimised at all
def collatz(n, length):
    if n == 1:
        return length
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    length += 1
    return collatz(n, length)


# t1 = time.time()
# maxlength = 0
# for i in range(1, 1000000):
#     length = collatz2(i, 1)
#     if length > maxlength:
#         maxlength = length
#         starting = i
# print(starting)
# t2 = time.time()
# print("Total time taken:", t1 - t2)


#  optimised using hash table
def collatz2(n, length, h):
    if n == 1:
        return length
    if n in h:
        return length + h[n]
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    return collatz2(n, length + 1, h)


maxlength = 0
h = {}
t1 = time.time()
for i in range(1, 1000000):
    length = collatz2(i, 1, h)
    if i not in h:
        h[i] = length
    if length > maxlength:
        maxlength = length
        starting = i
print(starting)
t2 = time.time()
print("Total time taken:", t2 - t1)
