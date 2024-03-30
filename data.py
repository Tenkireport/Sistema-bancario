from datetime import datetime

''' Mostrar o horario atual'''
print(datetime.now())

''' Mostrar individualmente'''

print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)


''' Criar uma data'''

data_ex = datetime(2025,3,20)

''' Converter string para data'''

#data_ex2 = datetime.strptime(input('Qual a data?'),'%d/%m/%Y')

#print(data_ex2)

''' Calcular a diferença da data'''
data_hoje = datetime.now()

data_nas = datetime(2024,12,25)

dias_passados = data_nas - data_hoje 
 

print(f'Dias passados des do meu nascimento = {dias_passados}')