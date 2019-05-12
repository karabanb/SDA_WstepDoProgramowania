
if __name__ == "__main__":


def erastothenes_sieve(n):
    if not n > 1:
        print('Bad data@')
        return
    sieve = []
    for i in range(n):
        sieve.append(True)
    for i in range(2, n//2):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False
    result_list = []
    for i in range(2, n):
        if sieve[i]:
            result_list.append(i)
    return result_list



