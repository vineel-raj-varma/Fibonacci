def fib(num):
    if num == 0:
        return print(0)
    elif num == 1:
        return print(1)
    else:
        num1 = 0
        num2 = 1
        lis = []
        for i in range(0, num):
            lis.append(num1)
            nth = num2 + num1
            num1 = num2
            num2 = nth
        return print(lis)


fib(8)

# If Input is 8
# Output will be
# [0, 1, 1, 2, 3, 5, 8, 13]
