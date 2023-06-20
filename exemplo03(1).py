'''Vamos criar um programa solicite um número real, 
calcule e que apresente: 
a) o valor absoluto; 
b) somente sua parte inteira; 
c) sua raiz quadrada; 
d) o fatorial desse número. 
'''

import math

num = float(input('Digite um número: '))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.trunc(math.fabs(inteiro)))
print('Valor absoluto = ', absoluto, "\nInteiro = ", inteiro, "\nRaiz = ", raiz, "\nFatorial = ", fatorial)

