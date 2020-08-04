# genPrimes


# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...



def genPrimes():
    yield 2
    isPrime = 3
    primes = []
    while True:
        if isPrime<4:
            yield isPrime
            primes.append(isPrime)
        else:
            for i in range(primes[-1], isPrime):
                if (isPrime % i) == 0:
                    break
            else:
                yield isPrime
        isPrime += 2



pp = genPrimes()

print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))
print(next(pp))

