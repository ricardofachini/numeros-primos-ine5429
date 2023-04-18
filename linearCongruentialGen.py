from time import time

class Gerador:
    def __init__(self, a=16807, c=12345) -> None:
        self.seed = round(time()*1000) # semente é o tempo atual em milissegundos
        self.a = a # a aleatório
        self.c = c # c arbitrário
        self.m = (2**31) - 1 # tamanho em bits do output, normalmente perto de 2 elevado a 31

    def inversive_congruential_generator(self):
        self.seed = (self.a * self.seed + self.c) % self.m # calcula o proximo X(n+1), baseado no
                                                           # Xn anterior, sendo X (0) a seed
        return self.seed
