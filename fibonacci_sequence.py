def fibonacci_sequence(n):
    num1 = 0
    num2 = 1
    fib_list = []
    for i in range(0, n):
        fib_list.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2

    return fib_list

a = fibonacci_sequence(8)
print(a)
