import random

''' Valores de 0.0 a 1.0'''
print(random.random())

''' Valor decimal do min ao max'''

print(random.uniform(1,10))

''' Valores aleatorios inteiros'''
print(random.randint(1, 10))

''' Escolher dentro de uma lista, usando k podemos modificar a quantidade de escolhas'''
cores = ['amarelo','azul','verde']
print(random.choice(cores))
print(random.choices(cores, k=2))

''' Embaralha uma lista'''
lista = [1,2,3,4,5]
print(f'Lista em ordem {lista}')

random.shuffle(lista)
print(f'lista embaralhada {lista}')
