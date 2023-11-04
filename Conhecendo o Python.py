print("Fala cria!")

#EX DE VARIÁVEL
age, name = (30, "Rafael")
print(f'Meu nome é {name} e tenho {age} anos.')

#EX DE CONST
#Em python não definirmos o tipo de var, para sinalizar uma const precisamos colocar tudo em uppercase e uma var tudo em lowercase
AGE = 50
NOME = "Rafão"
BRAZILIAN_STATES = ["RJ", "SP", "MG"]

#CONVERSÃO
#para float
preco = 5
preco = float(preco)
print(preco)

#para string
preco = 5
preco = str(preco)
print(preco)

#FUNÇÕES DE ENTRADA E SAÍDA
nome = input("Informe seu nome:")
idade = input("Informe sua idade:")
print(f"Meu nome é {nome} e tenho {idade} anos de idade.")