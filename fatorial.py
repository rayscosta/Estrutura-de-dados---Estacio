def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fat = n * fatorial(n - 1)
        return fat
    
print(fatorial(10))
    