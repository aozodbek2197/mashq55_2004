# 1-mashq
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([4,1,2,1,2]))
# 2-mashq
def hamming_weight(n):
    return bin(n).count('1')

print(hamming_weight(11))
# 3-mashq
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

print(is_happy(19))
