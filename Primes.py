def filter(n):
    if n<3:
        return []
    primes = [True for i in range(n)]
    primes[0] = False
    i = 2
    while i < n:
        while i < n and primes[i] is False:
            i=i+1
        for j in range(i + i, n, i):
            primes[j] = False
        i = i + 1
    return [i for i in range(2,n) if primes[i] is True]    

print(filter(100))