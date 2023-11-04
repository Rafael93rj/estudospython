#MANIPULANDO STRINGS
CURSO = "python"

print(CURSO.upper())
print(CURSO.lower())
print(CURSO.title())

#RETIRANDO ESPAÇOS
TEXTO = "   E ai    "

print(TEXTO.strip())
print(TEXTO.rstrip())
print(TEXTO.lstrip())

#TAMANHO DA STRING
print(len(TEXTO))

#MANIPULANDO VALORES DECIMAIS
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

#TRATANDO STRING COMO ARRAY
NOME = "Deividson Rafael Nascimento Santos"

print(NOME[0])
print(NOME[:10])
print(NOME[10:])
print(NOME[::-1])

#STRINGS MULTIPLAS (RESPEITA TAB E QUEBRA DE LINHAS)
eu = "Rafael"
mensagem = f"""
Olá, meu nome é {eu}
    E estou aqui de bob!
"""
print(mensagem)

