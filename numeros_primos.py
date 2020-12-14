"""O programa otimiza o número verificações entre os possíveis divisores e cada número.
Ao invés de verificar todos os números inferiores, basta começar a verificar a partir da raiz quadrada inteira.
Se um número for um quadrado perfeito, a sua raiz quadrada será o máximo divisor comum, então já é possível
desconsiderá-lo como um número primo e não necessário analisar os outros números maiores ou menores que ele.
Caso ele não seja um quadrado perfeito, a sua raiz quadrada inteira 'r' será suficiente para o intervalo [2, r] pertencente ao
conjunto dos naturais conferir se este número em questão é um número primo."""

import math

def intervalo_de_números_primos(início = 2, fim = 100):
    """(inteiro, inteiro) -> lista de inteiros"""
    primos = []
    if type(início) == int and type(fim) == int and início <= fim and início > 1:
        if início == 2:
            primos = [2]
            intervalo = list(range(3, fim + 1, 2)) #Ímpares no [3, fim]
        elif início % 2 == 0:
            intervalo = list(range(início + 1, fim + 1, 2)) #Ímpares no [início + 1, fim]
        else:
            intervalo = list(range(início, fim + 1, 2)) #Ímpares no [início, fim]

    else:
        raise ValueError("O intervalo deve ser um subconjunto do conjunto dos naturais e possuir extremidade inferior maior que 1 e menor ou igual a extremidade superior.")
        
    for i in intervalo:
        maior_divisor_do_quadrado = int(math.sqrt(i))
        ser_primo = True
        
        if maior_divisor_do_quadrado % 2 == 0:
            maior_divisor_do_quadrado = maior_divisor_do_quadrado - 1 #Caso a raiz quadrada inteira seja par, ela será alterada para o ímpar anterior. Pois todos os possíveis divisores devem ser ímpares.

        for num in range(maior_divisor_do_quadrado, 2, -2): #Intervalo de possíveis divisores - ]2, maior_divisor_do_quadrado].
            if i % num == 0:
                ser_primo = False
                break

        if ser_primo:
            primos.append(i)

    return primos
