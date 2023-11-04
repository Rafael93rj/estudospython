#FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()


#FOR COM RANGE (TABUADA DE 5)
for numero in range(0, 51, 5): #O primeiro parametro mostra de onde começa (opcional), o segundo onde termina e o último mostra a contagem (de quanto em quanto)
    print(numero, end=" ") #O "end" serve para deixar os itens em linha horizontal.


#WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    else:
        print("Obrigado por usar o nosso serviço!")

#WHILE COM BREAK
while True: #Loop infinito
    num = int(input("Digite um número: "))
    if num == 10: #Essa condição interrompe o laço de repetição caso o número seja igual a 10
        break
print(num)