# Implement prime_list(n). Return a list of all prime numbers from 
# 2 to n inclusive. A prime number has exactly two positive divisors.
# Students may need to research a simple primality test or 
# the Sieve of Eratosthenes.

def prime_list(n):

    
    if n < 2:
        return []

    prime_list = []

    for number in range(2,n+1):


        # is_Prime = True

        for divisor in range(2, int(number**0.5) + 1):

            if number % divisor == 0:
                # is_Prime = False
                break

        else:
            prime_list.append(number)

    return prime_list

# Test cases
print(prime_list(10))  # Output: [2, 3, 5, 7]
print(prime_list(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(prime_list(1))   # Output: []

        