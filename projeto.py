#Escolher o numero 
numero_secreto = int(input("digite o numero secreto"))


acertou = False

# Iniciar o loop do jogo
while not acertou:
    # Solicitar ao jogador uma tentativa
    tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    
    
    # Verificar se o jogador acertou
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}).")
        acertou = True
    elif tentativa < numero_secreto:
        print(f"Tente um número maior ({tentativa}).")
    else:
        print(f"Tente um número menor.({tentativa})")