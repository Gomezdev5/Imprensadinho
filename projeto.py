import random

# Gerar um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializar o contador de tentativas
tentativas = 0
acertou = False

# Iniciar o loop do jogo
while not acertou:
    # Solicitar ao jogador uma tentativa
    tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    
    # Incrementar o contador de tentativas
    tentativas += 1
    
    # Verificar se o jogador acertou
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas.")
        acertou = True
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")


    print("escolha outro numero de")
    numero