import random
from BlumBlumShub import BlumBlumShub
from fermat import fermat_is_prime
class MillerRabin:
    def __init__(self) -> None:
        self.n = None
        self.k = 5

    def is_prime(self, numero):
        self.n = numero
        r = 0   
        s = self.n - 1
        while s % 2 == 0:
            s //= 2
            r += 1

        for i in range(self.k):
            a = random.randint(1, self.n-1)
            x = pow(a, s, self.n) # a elevado a d módulo numero (n)
            if x == 1 or x == self.n-1:
                continue
            for j in range(r-1):
                x = pow(x, 2, self.n)
                if x == self.n-1:
                    break
            else:
                return "composto"
        return "provavelmente primo"

bbs = BlumBlumShub(1024)
mll = MillerRabin()
while True:
    n = bbs.gera_numero()
    result = mll.is_prime(n)
    result2 = fermat_is_prime(n)
    print("result mll: ", result)
    print("result fermat: ", result2)
    if result == result2:
        continue
    else:
        print("DIFERENTES!!!")
        break
