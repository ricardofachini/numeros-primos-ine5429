import random
def fermat_is_prime(n, k=10): # k número de testes do "a", arbitrário.
    for i in range(k): 
        a = random.randint(2, n-2) # escolhe um numero aleatorio maior que 2 e menor que o numero menos 2
        if pow(a, n-1, n) != 1: # o numero "aleatorio" elevado ao numero menos 1 modulo  numer
            return "composto" # se o modulo for diferente de 1, o numero com certeza é composto e não primo
    return "provavelmente primo" # se não foi achado que o número é composto, ele provavelmente é primo, mas sem certeza
