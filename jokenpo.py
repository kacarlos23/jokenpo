from random import randint
from time import sleep
from colorama import init, Fore, Back

# Inicializa o colorama
init(autoreset=True)

def jogar_novamente():

    while True:
        resposta = input('\nJogar novamente?\n(S)im (N)ao => ').lower().strip()

        if resposta.startswith('s'):
            return True
        elif resposta.startswith('n'):
            return False

        if not resposta:  # Quando o usuário nao digita nada
            print(Fore.RED + 'Erro: Nada foi digitado, tente novamente')
            continue

        try:
            if resposta not in ['s', 'n']:
                print(Fore.RED + 'Erro: Digite apenas "S" para Sim ou "N" para Não!')
                continue
            break
                
        except ValueError:  # Qualquer outro erro
            print('Erro: Entrada inválida!')

def jogada_valida():
    while True:
        entrada = input('Sua jogada: ') # Le a jogada do jogador como string
        
        if not entrada:  # Verifica se nao foi digitado nada
            print(Fore.RED + 'Erro: Nada foi digitado, tente novamente')
            continue
        
        if not entrada.isdigit():
            print(Fore.RED + 'Erro: Digite apenas números inteiros')
            continue
        
        jogador = int(entrada)
        
        if jogador not in [0, 1, 2]:
            print(Fore.RED + 'Erro: Digite apenas os números 0, 1 ou 2.')
        else:
            return jogador

# Menu
print(Fore.CYAN + ('=' * 31))
print(Fore.RED + '{:=^31}'.format('JOKENPÔ'))
print(Fore.CYAN + ('=' * 31))

# Variaveis de pontuação
pts_jogador = 0
pts_computador = 0
pts_empate = 0

# Loop que roda o jogo enquanto o usuario quiser
while True:

    print('''
    Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    ''')
    
    # Define a jogada do computador
    computador = randint(0,2)
    
    # Valida a jogada do jogador
    jogador = jogada_valida()

    resultados = {
        # Pedra
        0: {
            0: (Fore.CYAN + 'Conseguiu empatar dessa vez...', 'empate'),
            1: (Fore.RED + 'A máquina ganhou >:)', 'derrota'),
            2: (Fore.GREEN + 'Parabéns, você venceu :D', 'vitoria')
        },
        
        # Papel
        1: {
            0: (Fore.GREEN + 'Parabéns, você venceu :D', 'vitoria'),
            1: (Fore.CYAN + 'Conseguiu empatar dessa vez...', 'empate'),
            2: (Fore.RED + 'A máquina ganhou >:)', 'derrota')
        },

        # Tesoura
        2: {
            0: (Fore.RED + 'A máquina ganhou >:)', 'derrota'),
            1: (Fore.GREEN + 'Parabéns, você venceu :D', 'vitoria'),
            2: (Fore.CYAN + 'Conseguiu empatar dessa vez...', 'empate')
        }
    }
    
    # Armazena os valores do dicionario nas variaveis
    mensagem, resultado = resultados[jogador][computador] 
    
    # Adiciona pontuação do vencedor
    if resultado == 'vitoria':
        pts_jogador += 1
    elif resultado == 'empate':
        pts_empate += 1
    elif resultado == 'derrota':
        pts_computador += 1

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 15)

    # Mostra quem venceu
    print(mensagem)

    # Menu da tabela
    print('{:=^31}'.format('TABELA DE PONTUAÇÃO'))
    print(f'=> Jogador: ', pts_jogador)
    print(f'=> Máquina: ', pts_computador)
    print(f'=> Empates: ', pts_empate)

    if jogar_novamente():
        print(Fore.YELLOW + 'Então vamos mais uma :D')
    else:
        print(Fore.YELLOW + 'Até a próxima... :D')
        sleep(5)
        break
