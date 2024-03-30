#Sistema bancario V 0.0.1

#Variaveis
saldo = 0
limite = 500
saidas = []
entradas = []
limite_saque = 3

#Menu

while True:
    
    print("===== Banco CM =====\n")
    print('==Opçoes==\nDeposito (0)\nSaque  (1)\nExtrato(2)\nSair(3)\n')
    op = input(':')
    
    #deposito
    if op == '0':
        deposito = int(input('Deposito:'))
        entradas.append(deposito)
        saldo += deposito
       
    #Saque    
    if op == '1':
        while limite_saque > 0:
            saque = int(input('Valor de retirada:'))
            if saque > 500 or saque < 0:
                print('Valor invaldio ou acima do permitido')
                break
            else:
                
                if saldo >= saque:
                    saidas.append(saque)
                    saldo -= saque
                    limite_saque -= 1
                    break
                else:
                    print('Sem saldo o suficiente')
                    break
        if limite_saque == 0:
            print('limite diario atingido')
                         
    #extrato
    if op == '2':
        
        print('saques\n')
        for e in entradas:
            print(f'Deposito de R$ {e}')
        for e in saidas:
            print(f'Saque de R$ {e}') 
        print(f'Saldo atual: R$ {saldo}')
        
    
    
    
    #sair do programa
    if op == '3':
        break
    