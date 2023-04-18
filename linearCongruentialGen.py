from time import time
class Gerador:
    def __init__(self, bit_size, a=6364136223846793005, c=12345) -> None:
        self.seed = round(time()*1000) # semente é o tempo atual em milissegundos
        self.a = a # a aleatório
        self.c = c
        self.m = 2**bit_size # tamanho em bits do output

    def inversive_congruential_generator(self):
        self.seed = (self.a * self.seed + self.c) % self.m # calcula o proximo Xn
        return self.seed
gerador = Gerador(40)
for i in range(1):
    randn = gerador.inversive_congruential_generator()
    print(randn)
