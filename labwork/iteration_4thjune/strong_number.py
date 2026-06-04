num = int(input("Enter a number: "))

n = num
factorial_sum = 0

while num > 0:
    digit = num % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_factorial += factorial
    num = num // 10

if sum_factorial == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")
