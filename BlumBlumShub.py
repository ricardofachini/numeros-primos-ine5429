from time import time
from math import gcd
class BlumBlumShub:

    def __init__(self, bit_size) -> None:
        self.seed = round(time()*1000) # semente inicial é o tempo atual no PC em milissegundos
        self.bit_size = bit_size # tamanho de bit para a saída
        p = 49979687 # numero primo
        q = 32416190071 # numero primo
        self.m = p % q # modulo a ser calculado na seed é (p mod q)

    def escolhe_seed(self):
        # escolhe uma seed, sendo um numero co-primo a M
        while True:
            self.seed = (self.seed**2) % self.m
            if gcd(self.seed, self.m) == 1: # verifica se a semente é coprimo de m
                break

    def gera_numero(self):
        bits = []
        self.escolhe_seed() # escolhe a seed coprimo ao modulo M
        for _ in range(self.bit_size):
            self.seed = (self.seed**2) % self.m # calcula o numero pseudoaleatorio
            bit = self.seed % 2 # calcula o bit e armazena na lista de bits
            bits.append(bit)
            result = int(''.join(str(b) for b in bits), 2) # junta os n_bits bits do numero aleatorio
        return result
bbs = BlumBlumShub(4096) # parametro é a largura de bits do output