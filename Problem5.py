number = 2520
numberNotFound = True
test = 0
while numberNotFound:
    for i in range(1,20):
        if number % i != 0:
            number += 1
            test = 0
        else:
            test += 1
        if test == 20:
            print(number)
