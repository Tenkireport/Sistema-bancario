
#variaveis
saldo =         0
depositos =     []
saques =        []
limite_saques = 3
ops =           ['d','s','e','q']


#menu
def menu():

    print('====== Banco CM V2 ======\n')
    print('==== Opcoes==== \n')
    print('[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n')

#deposito
def deposito():
    global saldo
    x = input('Digite o valor do deposito:')
    if x.replace('.','').isdigit():
        valor = float(x)
        depositos.append(valor)
        saldo += valor
    else:
        print('Valor invalido')

#sacar
def sacar():
    global saldo
    global limite_saques
    while limite_saques > 0:
        saque = input('Valor a ser retirado: ')
        if saque.replace('.','').isdigit():
            valor_saque = float(saque)
            if saldo > valor_saque:
                saques.append(valor_saque)
                saldo -= valor_saque
                limite_saques -= 1
                break
            elif valor_saque > 500:
                print('Valor muito alto para saque')
                break
            elif saldo < valor_saque:
                print('Saldo insuficiente')
                break
        else:
            print('Digite apenas numeros')
            break
    if limite_saques == 0:
        print('Limite de saque diario atingido')
        
#extrato
def extrato():
    if len(depositos) == 0:
        print('Sem depositos recentes')
    else: 
        for i in depositos:
            print(f'Depositos feitos R$ {i:.2f}')
    if len(saques) == 0:
        print('Sem saques efetuados')
    else:
        for i in saques:
            print(f'Saques efetuados R$ {i:.2f}')
    print(f'Saldo atual R$ {saldo:.2f}')
        


#loop principal

while True:
    menu()
    op = input(':')
    if op in ops:
        if op == 'd':
            deposito()
            
        if op == 's':
            sacar()
        
        if op == 'e':
            extrato()
            
        if op == 'q':
            break
            
    
    