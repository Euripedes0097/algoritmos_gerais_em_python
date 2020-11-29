#O programa otimiza o número verificações entre os possíveis divisores e cada número.
#Ao invés de verificar todos os números inferiores, basta começar a verificar a partir da raiz quadrada inteira.
#Se um número for um quadrado perfeito, a sua raiz quadrada será o máximo divisor comum, então já é possível
#desconsiderá-lo como um número primo e não necessário analisar os outros números maiores ou menores que ele.
#Caso ele não seja um quadrado perfeito, a sua raiz quadrada inteira 'r' será suficiente para o intervalo [2, r] pertencente ao
#conjunto dos naturais conferir se este número em questão é um número primo.

import math

primos = [2]

intervalo = list(range(3,100,2)) #ímpares no [3, 100)

for i in intervalo:
    maior_divisor_do_quadrado = int(math.sqrt(i))
    ser_primo = True
    
    for num in range(maior_divisor_do_quadrado, 1, -1):
        if i % num == 0:
            ser_primo = False
            break

    if ser_primo and i > 1:
        primos.append(i)

#exibir a lista de números primos
for p in primos:
    print(p, end=', ')
