import random
class MillerRabin:
    def __init__(self) -> None:
        self.n = None
        self.k = 5 # define a precisão do teste, k maior é mais preciso, mas mais lento

    def is_prime(self, numero):
        self.n = numero
        r = 0   
        s = self.n - 1
        while s % 2 == 0: # achar um s e r tal que n - 1 seja igual a ((2^r) * s)
            s //= 2
            r += 1

        for _ in range(self.k):
            a = random.randint(1, self.n-1)
            x = pow(a, s, self.n) # a elevado a d módulo numero (n)
            if x == 1 or x == self.n-1:
                continue
            for _ in range(r-1):
                x = pow(x, 2, self.n) # x² mod n
                if x == self.n-1: # se x^2 mod n for igual ao numero - 1, ele provavelmente é primo
                    break
            else:
                return "composto"
        return "provavelmente primo"
