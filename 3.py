primes = [3] # ignore 2 since number is odd

def find_prime():
    i = primes[-1]
    while 1:
        i += 2
        is_prime = True
        for prime in primes:
            if (i) % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(i)
            return

def find_largest_prime_factor(num):
    while 1:
        prime = primes[-1]
        while 1:
            if num % prime == 0:
                num /= prime
                if (round(num) == 1): # handle possible floating point errors
                    print(prime)
                    return
            else:
                break
        find_prime()

num = 600851475143
find_largest_prime_factor(num)