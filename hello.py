def fibonacci(n):
    '''Finally some recursive action! (showoff :)'''
    if n < 0:
        raise Exception("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n-1)
