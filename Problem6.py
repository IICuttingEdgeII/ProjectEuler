square_sum = 0
sum_square = 0

for i in range(1, 101):
    square_sum += i
    sum_square += i**2

answer = (square_sum**2) - sum_square
print(answer)