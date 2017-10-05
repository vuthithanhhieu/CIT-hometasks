# function
def divide_and_conquer(p_arr, p_prime_num):

    v_old_num = 0

    while p_prime_num != v_old_num:
        v_old_num = p_prime_num
        v_start = len(p_arr) + 1

        for i in range(p_prime_num, len(p_arr)):

            if (i + 1) % p_prime_num == 0:
                v_start = i
                break

        for i in range(v_start, len(p_arr), p_prime_num):
            p_arr[i] += 1

        for k in range(p_prime_num + 1, len(p_arr)):
            if p_arr[k - 1] == 0:
                p_prime_num = k
                break

# main
def main():

    print("Enter N:")
    v_num = int(input())

    v_arr = []
    for i in range(v_num):
        v_arr.append(0)

    divide_and_conquer(v_arr, 2)

    for i in range(len(v_arr)):
        if v_arr[i] == 0:
            print(i + 1)


main()
print("done")
