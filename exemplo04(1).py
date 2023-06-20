'''Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, 
para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), 
o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão:
volume=h/3*(Bmaior**2 +  Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5) 
'''
    

#entrada de dados
h = float(input("Digite a altura do tronco da pirâmide: "))
Bmenor = float(input("Digite a base menor do tronco da pirâmide: "))
Bmaior = float(input("Digite a base maior do tronco da pirâmide: "))
#processamento
volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
#saida
print("Volume = ", volume)