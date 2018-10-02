# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000
import time


def sum_of_multiples(n):
    tmp_sum = sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)
    return tmp_sum


def main():
    n = 100
    start_time = time.time()
    print(sum_of_multiples(n))
    print(time.time() - start_time)

if __name__ == '__main__':
    main()