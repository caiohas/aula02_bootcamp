# Instruções:

CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que insira seu nome.
nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Acho que você digitou seu nome errado.")
    exit()

if len(nome_usuario) == 0:
    print("Você não digitou nada, cara!")
    exit()

if nome_usuario.isspace():
    print("Você digitou só espaço, amigão!")
    exit()

# 2) Solicita ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
try:
    salario_usuario = float(input("Digite o valor do seu salário: "))
    if salario_usuario < 0:
        print("Por favor, digite um valor positivo para o salário.")
        exit()
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# 3) Solicita ao usuário para inserir a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
try:
    bonus_usuario = float(input("Digite o valor do bônus recebido: "))
    if bonus_usuario < 0:
        print("Por favor, digite um valor positivo para o bônus.")
        exit()
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

# 4) Calcule o valor do bonus final.
valor_bonus =  CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem.
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus} reais.")