# def primary(number, list_primes):
#     for i in list_primes:
#         if number % int(i) == 0:
#             return False
#     return True
#
#
# list_primes = ['2']
# for i in range(3, 1000000):
#     if primary(i, list_primes):
#         list_primes.append(str(i))
# print(list_primes)
# list_out = []
#
# for prime in list_primes[4:]:
#     temp = 0
#     for i in range(1, len(prime)):
#         if prime[:len(prime) - i] not in list_primes or prime[len(prime) - i:] not in list_primes or prime[
#             0] not in list_primes or prime[-1] not in list_primes:
#             temp += 1
#             break
#     if temp == 0:
#         list_out.append(int(prime))
#         if len(list_out) == 11:
#             break
# print(len(list_out), sum(list_out), list_out)

# /\ moje \/ nie moje


def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 or n % int(n / i) == 0: return False
    return True


nums, i = [], 10
while len(nums) < 11:
    stnum, is_num_corr = str(i), True
    for j in range(len(stnum)):
        if not is_prime(int(stnum[:len(stnum) - j])) or not is_prime(int(stnum[j:])):
            is_num_corr = False
            break
    if is_num_corr:
        nums.append(i)
    i += 1

print(sum(nums), nums[-1])
