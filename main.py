import random # Irá permitir embaralhar as cartas

cartas = [
    "🦔", "🦔", "🐴", "🐴",
    "🦁", "🦁", "🐨", "🐨",
    "🐼", "🐼", "🦓", "🦓",
    "🐭", "🐭", "🐷", "🐷"
]

random.shuffle(cartas) # Embaralha as cartas

tabuleiro = [] 

# Monta o tabuleiro com as cartas embaralhadas 
for i in range(0, 16, 4): # Loop
    linha = cartas[i:i+4] # contador
    tabuleiro.append(linha) # Monta o tabuleiro

visivel = [['🟥'] * 4 for i in range(4)]

for linha in tabuleiro: # Percorre cada linha do tabuleiro real
    linha_visivel = ['🟥'] * 4 # Cria uma linha escondida
    visivel.append(linha_visivel)

def mostrar(tabuleiro):
    for linha in tabuleiro: 
        print(" ".join(linha)) # Mostra o tabuleiro



def jogar ():
    while True:
     mostrar(visivel)
   
     linha = int(input("Escolha á linha (1-4): ")) # Pede a posição do jogador
     coluna = int(input("Escolha a coluna (1-4): "))
     
     linha -=1 
     coluna -=1
    
     if visivel[linha][coluna] != '🟥':
         print("Essa carta já foi escolhida! Por favor, tente outra")
         continue
    
     visivel[linha][coluna] = tabuleiro[linha][coluna] # Revela a carta escolhida

     linha_dois = int(input("Escolha a segunda linha (1-4): ")) # Pede a posição do jogador para a segunda carta
     coluna_dois = int(input("Escolha a segunda coluna (1-4): "))

     linha_dois -=1
     coluna_dois -=1

     visivel[linha_dois][coluna_dois] = tabuleiro[linha_dois][coluna_dois] # Revela a segunda carta escolhida
     mostrar(visivel) # Mostra o tabuleiro com as caratas viradas 

     if tabuleiro[linha][coluna] == tabuleiro[linha_dois][coluna_dois]: # Verifica se as cartas são iguais
        print (" Par encontrado!🥳 ")

     else: 
        print (" Ops! A cartas não são iguais.🥹 ")
        visivel[linha][coluna] = '🟥' # Esconde as cartas novamente

     pares_encontrados = sum(
        1 for r in range(4) for c in range(4) # Conta quantos pares foram percorridos
        if visivel[r][c] != '🟥' # r: row - Linha, c: coluna - column
     ) //2

     if pares_encontrados == 8: 
         print("Parabéns! Você encontrou todos os pares!🎉")
         break
    
jogar()
