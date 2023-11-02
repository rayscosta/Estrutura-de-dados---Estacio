def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        f = fibonacci(n - 1) + fibonacci(n - 2)
        return f

print(fibonacci(7))