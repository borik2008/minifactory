import random

setka = [[0] * 15] * 8
numbers = 0
while True:
    num1 = random.randint(0, 7)
    num2 = random.randint(0, 14)
    if setka[num1][num2] == 0:
        setka[num1][num2] = 1
        numbers += 1
    if numbers == 10:
        break
print(numbers)