'''Vamos criar um programa que 
apresente o resultado da raiz quadrada 
de um número digitado pelo usuário. 
'''

import math # importa biblioteca matemática
num = float(input('Digite um número: '))
raiz = math.sqrt(num) #uso da função matemática

print('Raiz de: ', num, " é: ", raiz)