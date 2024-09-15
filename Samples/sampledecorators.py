def cache(func):
    results = {}
    def wrapper(*args):
        if args in results:
            return results[args]
        result = func(*args)
        results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + " "+ fibonacci(n-2)

print(fibonacci(35))  # Much faster with caching