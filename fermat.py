import random
from BlumBlumShub import BlumBlumShub

def fermat_is_prime(n, k=10):
    for i in range(k):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return "composto"
    return "provavelmente primo"

bbs = BlumBlumShub(512)
while True:
    result = fermat_is_prime(187931327021)
    if result == "composto":
        continue
    else:
        print(result)
        break