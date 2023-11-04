#IF e ELSE
saldo = 2000
saque = float(input("Informe o valor de saque: "))

if saque > saldo:
    print("Saldo insuficiente")
else:
    print("Pegue seu dinheiro no caixa")

#ELIF (SE NÃO, SE)
MAIOR_IDADE = 18
user = int(input("Digite a sua idade: "))

if user >= MAIOR_IDADE:
    print("Parabéns, você pode tirar a CNH!")
elif user == 17:
    print("Ops, você só tem idade para assistir as aulas teóricas.")
else:
    print("Que pena, você ainda não pode tirar a CNH")

#IF ANINHADO
conta_normal = True
conta_universitaria = False

saldo_dois = 2000
saque_dois = 2500
cheque_especial = 450

if conta_normal:
    if saldo_dois >= saque_dois:
        print("Saque realizado com sucesso!")
    elif saque_dois <= (saldo_dois + cheque_especial):
        print("Saque realizado com o uso do Cheque Especial.")
    else: 
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo_dois >= saque_dois:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

#IF TERNÁRIO
saldo_tres = 2000
saque_tres = 2500

status = "Sucesso" if saldo_tres >= saque_tres else "Falha"
print(f"{status} ao realizar o saque!")