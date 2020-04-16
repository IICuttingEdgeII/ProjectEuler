# Pythagorean Triplet

def pythagoreanTriplet():
    a = []
    b = []
    c = []
    squares = []
    answer = -1
    for p in range(1, 601):
        squares.append(p ** 2)
    for i in range(len(squares)):
        for j in range(len(squares)):
            a_plus_b = squares[i] + squares[j]
            if a_plus_b in squares:
                a.append(squares[i] ** 0.5)
                b.append(squares[j] ** 0.5)
                c.append(a_plus_b ** 0.5)
    for k in range(len(c)):
        if a[k] + b[k] + c[k] == 1000:
            answer = (a[k] * b[k] * c[k])
    return answer
print(pythagoreanTriplet())