import time

def sum_of_multiples(n):
    k_3 = n // 3
    k_5 = n // 5

    print(k_5)

    tmp_sum_3 = (1 + k_3)*k_3*3
    tmp_sum_5  = (1 + k_5)*k_5*5

    return (tmp_sum_5 + tmp_sum_3)//2

def main():
    n = 1000
    start_time = time.time()
    print(sum_of_multiples(n - 1))
    print(time.time() - start_time)

if __name__ == '__main__':
    main()