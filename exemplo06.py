'''Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis separadas). 
Calcule e mostre a idade expressa apenas em dias. 
Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
'''
anos = int(input('Digite a sua idade: '))
meses = int(input('Digite quantos meses vc tem: '))
dias = int(input('Digite quantos dias vc tem: '))
print("Você tem = ", (anos*365+meses*30+dias))