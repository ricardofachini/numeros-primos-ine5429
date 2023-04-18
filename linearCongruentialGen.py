from time import time

class Gerador:
    def __init__(self, a=16807, c=12345) -> None:
        self.seed = round(time()*1000) # semente é o tempo atual em milissegundos
        self.a = a # a aleatório
        self.c = c
        self.m = (2**31) - 1 # tamanho em bits do output

    def inversive_congruential_generator(self):
        self.seed = (self.a * self.seed + self.c) % self.m # calcula o proximo X(n+1), baseado no
                                                           # Xn anterior, sendo X (0) a seed
        return self.seed
gerador = Gerador() # 40 bits -> muda-se esse numero para uma saída de tamanho diferente
for i in range(1):
    randn = gerador.inversive_congruential_generator()
    print(randn)
    #print(size(randn))
