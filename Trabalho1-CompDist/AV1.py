import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def disponibilidade(n, k, p):
    #n = número total de servidores replicados ou instâncias do serviço
    #k = número mínimo de servidores que precisam estar disponíveis ao mesmo tempo para que o serviço funcione corretamente (k=1 (pelo menos um servidor funciona)) (k=n (todos os servidores funcionam))
    #p = Probabilidade de Disponibilidade de um Servidor 
    A = 0
    for i in range(k, n+1):
        A += comb(n, i) * (p**i) * ((1 - p)**(n - i)) # FORMULA (explicação abaixo)
    return A

# comb(n, i) -> coeficiente binomial (quantas maneiras pode-se escolher i servidores disponiveis entre n servidores);
# (p**i) -> Isso representa a probabilidade de exatamente i servidores estarem indisponiveis.  Cada servidor tem probabilidade p de estar disponível, e a probabilidade de i servidores estarem disponíveis é p multiplicado por si mesmo i vezes, ou p^i .
# ((1 - p)**(n - i)) -> A probabilidade de um servidor esta disponivel é 1 - p, entao para que n - i servidores estejam disponiveis, multiplicamos (1-p) por si mesmo n - i vezes, ou seja ((1 - p)**(n - i))

plt.figure(figsize=(8, 5))

N = [3, 5]
K = [1, 3]

P = [0.2, 0.5, 0.8]

for n in N:
    for k in K:
        disponibilidade_values = [disponibilidade(n, k, p) for p in P]
        plt.bar([f'p={p}' for p in P], disponibilidade_values, label=f'n={n}, k={k}', alpha=0.7)

plt.title('Disponibilidade do Serviço para Diferentes Valores de n e k')
plt.xlabel('Probabilidade de Disponibilidade de um Servidor (p)')
plt.ylabel('Disponibilidade do Serviço')
plt.legend()
plt.show()
