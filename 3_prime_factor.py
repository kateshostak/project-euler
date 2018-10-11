# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math


def prime_factor(n):
    prime_factors = list()
    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n = n//i
        else:
            i +=1

    return  prime_factors

def main():
    n = 600851475143
    print(prime_factor(n))

if __name__ == '__main__':
    main()