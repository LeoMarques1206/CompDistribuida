import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def disponibilidade(n, k, p):
    #n = número total de servidores replicados ou instâncias do serviço
    #k = número mínimo de servidores que precisam estar disponíveis 
    #p = Probabilidade de Disponibilidade de um Servidor 
    A = 0
    for i in range(k, n+1):
        A += comb(n, i) * (p**i) * ((1 - p)**(n - i))
    return A

# comb(n, i) -> coeficiente binomial (quantas maneiras pode-se escolher i servidores disponiveis entre n servidores);
# (p**i) -> Isso representa a probabilidade de exatamente i servidores estarem indisponiveis.  Cada servidor tem probabilidade p de estar disponível, e a probabilidade de i servidores estarem disponíveis é p multiplicado por si mesmo i vezes, ou p^i .
# ((1 - p)**(n - i)) -> Isso representa a probabilidade de que exatamente n - i servidores estejam indisponíveis, já que a probabilidade de um servidor estar indisponível é (1 - p).


plt.figure(figsize=(10, 6))

N = [3, 5] 
P = np.linspace(0.1, 1.0, 100)  

for n in N:
    ks = [1, n, (n//2) + 1] 
    for k in ks:
        disponibilidade_values = [disponibilidade(n, k, p) for p in P]
        plt.plot(P, disponibilidade_values, label=f'n={n}, k={k}')

plt.title('Disponibilidade do Serviço para k=1, k=n, e k=(n/2)+1')
plt.xlabel('Probabilidade de UM Servidor estar disponivel (p)')
plt.ylabel('Disponibilidade do Serviço')
plt.legend(title="Configurações (n, k)")
plt.grid(True) 
plt.show()
