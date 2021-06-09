# importando biblioteca para manipular arquivos de texto e encontrar diretórios
import os
import time 

# matriz para guardar as posições do tabuleiro
matriz = [
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "]]
# função que armazena a quantidade de jogadas edefutadas
actions = 0 
game_status = False
default_delay = 2

# função que cria um novo usuário
def newPlayer(username):
	u_name = username.upper() # transsformando o texto em caixa alta para manter um padrão
	if os.path.isfile("./{}.txt".format(u_name)): # validando se o arquivo ja existe
		print("Este username já existe, por favor, escolha outro 😷 ." ,end="\n") ## caso o arquivo já existe, retorna uma mensagem informando isto
	else:
		new_file = open("./{}.txt".format(u_name), "w") # criando novo arquivo com o username informado
		# uma linha ira guardar as vitórias enquanto a outra, as derrotas do usuário	
		new_file.write("0\n")
		new_file.write("0\n")
		new_file.close() # fechando arquivo
		print("Usuário {} criado com sucesso, tenha um bom jogo 🙂" .format(username),end="\n")
# deletando usuário existente
def delPlayer(username):
    d_u_name = username.upper() # transformando em caixa alta antes de buscar o arquivo
    if os.path.isfile("./{}.txt".format(d_u_name)):
        os.remove("./{}.txt".format(d_u_name))
        print("Usuário deletado com sucesso 🙂",end="\n")
        time.sleep(default_delay)
        return __main__()
    else:
        print("Usuário não encontrado, tente novamente 😓",  end="\n")
# buscando se um usuário é válido
def searchPlayer(username):
    d_u_name = username.upper() # transformando em caixa alta antes de buscar o arquivo
    if os.path.isfile("./{}.txt".format(d_u_name)):
        return True
    else:
        return False 
        #print("Usuário não encontrado, tente novamente 😓",  end="\n")
# interface do jogo
def printGame():
    try:
        os.system("cls") or None # no windowns 
        #os.system("clear") or None # no linux
    except Exception:
        print("-*-"*30)
 
    for i in range(0,5):
        print(" {} | {} | {} | {} | {} ".format(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3],matriz[i][4]), end="\n")
        if i < 4 :
            print("-"*20, end="\n")
# função responsável por validar o status do jogo. interar a quantidade de jogadas . validar se algum dos usuários venceu a partida
def handlerV():
    global actions
    actions +=1
    if (matriz[0][0]=="x" and matriz[0][1]=="x" and matriz[0][2]=="x" and matriz[0][3]=="x") or (matriz[0][1]=="x" and matriz[0][2]=="x" and matriz[0][3]=="x" and matriz[0][4]=="x")  or (matriz[1][0]=="x" and matriz[1][1]=="x" and matriz[1][2]=="x" and matriz[1][3]=="x") or (matriz[1][1]=="x" and matriz[1][2]=="x" and matriz[1][3]=="x" and matriz[1][4]=="x") or (matriz[2][0]=="x" and matriz[2][1]=="x" and matriz[2][2]=="x" and matriz[2][3]=="x") or (matriz[2][1]=="x" and matriz[2][2]=="x" and matriz[2][3]=="x" and matriz[2][4]=="x") or (matriz[3][0]=="x" and matriz[3][1]=="x" and matriz[3][2]=="x" and matriz[3][3]=="x") or (matriz[3][1]=="x" and matriz[3][2]=="x" and matriz[3][3]=="x" and matriz[3][4]=="x") or (matriz[4][0]=="x" and matriz[4][1]=="x" and matriz[4][2]=="x" and matriz[4][3]=="x") or (matriz[4][1]=="x" and matriz[4][2]=="x" and matriz[4][3]=="x" and matriz[4][4]=="x") or (matriz[0][0]=="x" and matriz[1][0]=="x" and matriz[2][0]=="x" and matriz[3][0]=="x") or (matriz[1][0]=="x" and matriz[2][0]=="x" and matriz[3][0]=="x" and matriz[4][0]=="x") or (matriz[0][1]=="x" and matriz[1][1]=="x" and matriz[2][1]=="x" and matriz[3][1]=="x") or (matriz[1][1]=="x" and matriz[2][1]=="x" and matriz[3][1]=="x" and matriz[4][1]=="x") or (matriz[0][2]=="x" and matriz[1][2]=="x" and matriz[2][2]=="x" and matriz[3][2]=="x") or (matriz[1][2]=="x" and matriz[2][2]=="x" and matriz[3][2]=="x" and matriz[4][2]=="x") or (matriz[0][3]=="x" and matriz[1][3]=="x" and matriz[2][3]=="x" and matriz[3][3]=="x") or (matriz[1][3]=="x" and matriz[2][3]=="x" and matriz[3][3]=="x" and matriz[4][3]=="x") or (matriz[0][4]=="x" and matriz[1][4]=="x" and matriz[2][4]=="x" and matriz[3][4]=="x") or (matriz[1][4]=="x" and matriz[2][4]=="x" and matriz[3][4]=="x" and matriz[4][4]=="x") or (matriz[0][0]=="x" and matriz[1][1]=="x" and matriz[2][2]=="x" and matriz[3][3]=="x") or (matriz[1][1]=="x" and matriz[2][2]=="x" and matriz[3][3]=="x" and matriz[4][4]=="x") or (matriz[0][4]=="x" and matriz[1][3]=="x" and matriz[2][2]=="x" and matriz[3][1]=="x") or (matriz[4][0]=="x" and matriz[3][1]=="x" and matriz[2][2]=="x" and matriz[1][3]=="x"):
        print("vitória jogador X")
    elif(matriz[0][0]=="o" and matriz[0][1]=="o" and matriz[0][2]=="o" and matriz[0][3]=="o") or (matriz[0][1]=="o" and matriz[0][2]=="o" and matriz[0][3]=="o" and matriz[0][4]=="o") or (matriz[1][0]=="o" and matriz[1][1]=="o" and matriz[1][2]=="o" and matriz[1][3]=="o") or (matriz[1][1]=="o" and matriz[1][2]=="o" and matriz[1][3]=="o" and matriz[1][4]=="o") or (matriz[2][0]=="o" and matriz[2][1]=="o" and matriz[2][2]=="o" and matriz[2][3]=="o") or (matriz[2][1]=="o" and matriz[2][2]=="o" and matriz[2][3]=="o" and matriz[2][4]=="o") or (matriz[3][0]=="o" and matriz[3][1]=="o" and matriz[3][2]=="o" and matriz[3][3]=="o") or (matriz[3][1]=="o" and matriz[3][2]=="o" and matriz[3][3]=="o" and matriz[3][4]=="o") or (matriz[4][0]=="o" and matriz[4][1]=="o" and matriz[4][2]=="o" and matriz[4][3]=="o") or (matriz[4][1]=="o" and matriz[4][2]=="o" and matriz[4][3]=="o" and matriz[4][4]=="o") or (matriz[0][0]=="o" and matriz[1][0]=="o" and matriz[2][0]=="o" and matriz[3][0]=="o") or (matriz[1][0]=="o" and matriz[2][0]=="o" and matriz[3][0]=="o" and matriz[4][0]=="o") or (matriz[0][1]=="o" and matriz[1][1]=="o" and matriz[2][1]=="o" and matriz[3][1]=="o") or (matriz[1][1]=="o" and matriz[2][1]=="o" and matriz[3][1]=="o" and matriz[4][1]=="o") or (matriz[0][2]=="o" and matriz[1][2]=="o" and matriz[2][2]=="o" and matriz[3][2]=="o") or (matriz[1][2]=="o" and matriz[2][2]=="o" and matriz[3][2]=="o" and matriz[4][2]=="o") or (matriz[0][3]=="o" and matriz[1][3]=="o" and matriz[2][3]=="o" and matriz[3][3]=="o") or (matriz[1][3]=="o" and matriz[2][3]=="o" and matriz[3][3]=="o" and matriz[4][3]=="o") or (matriz[0][4]=="o" and matriz[1][4]=="o" and matriz[2][4]=="o" and matriz[3][4]=="o") or (matriz[1][4]=="o" and matriz[2][4]=="o" and matriz[3][4]=="o" and matriz[4][4]=="o") or (matriz[0][0]=="o" and matriz[1][1]=="o" and matriz[2][2]=="o" and matriz[3][3]=="o") or (matriz[1][1]=="o" and matriz[2][2]=="o" and matriz[3][3]=="o" and matriz[4][4]=="o") or (matriz[0][4]=="o" and matriz[1][3]=="o" and matriz[2][2]=="o" and matriz[3][1]=="o") or (matriz[4][0]=="o" and matriz[3][1]=="o" and matriz[2][2]=="o" and matriz[1][3]=="o"):
        print("vitória jogador O")
    elif actions >= 26:
        print("empate")
    else:
        printGame()
# função que reserva o espaço na matriz caso ele esteja livre
def doSomething(user, linha , coluna):
    if matriz[linha][coluna] != " ":
        print("⚠ Esta posição já foi reservada anteriormente. Escolha outra posição ⚠")  
    else:
        matriz[linha][coluna] = user
        handlerV()
# função que inicia o jogo
def gameInit():
    global game_status
    if game_status:
        return print("Game já foi iniciado anteriormente, tente novamente 🧐", end="\n")
   
    first_player = input("Digite o nome do primeiro usuário [X]: ")
    second_player = input("Digite o nome do primeiro usuário [0]: ")

    # validando se os us usuários existem
    first = searchPlayer(str(first_player).upper())   
    second = searchPlayer(str(second_player).upper())   
    if first == False or second == False:
        if first == False:
            print("Usuário {} não encontrado 😓".format(first_player),  end="\n")
            time.sleep(default_delay)
            print("Não se preocupe, estamos criando este usuário para você 🙂".format(first_player),  end="\n")
            time.sleep(default_delay)
            newPlayer(first_player)
        if second == False: 
            print("Usuário {} não encontrado 😓".format(second_player),  end="\n")
            time.sleep(default_delay)
            print("Não se preocupe, estamos criando este usuário para você 🙂".format(second_player),  end="\n")
            time.sleep(default_delay)
            newPlayer(second_player)
        time.sleep(default_delay*3)
        return os.system("cls")
    else:
	    game_status = True

    while game_status:
        lin = int(input("Digite qual a linha para o usuário X: "))
        col = int(input("Digite qual a coluna para o usuário X: "))
        doSomething("x", lin-1, col-1)

## FUNÇÃO PRINCIPAL 
def __main__():
    os.system('cls')
    #os.system('clear') # no linux
    print("-"*40,end="\n")
    print("JOGO DA VELHA EM PYTHON",end="\n")
    print("-"*40,end="\n")
    print("-"*5+" 1 - Criar novo usuário",end="\n")
    print("-"*5+" 2 - Deletar usuário",end="\n")
    print("-"*5+" 3 - Buscar histórico",end="\n")
    print("-"*5+" 4 - Iniciar um novo jogo",end="\n")
    print("-"*5+" 5 - Sobre este jogo",end="\n")

    user_option = int(input("-"*5+" Digite uma das opções: "))

    if user_option > 5:
        print("Ops! parece que esta não é uma opção válida, tente novamente 😓",  end="\n")
        time.sleep(default_delay*2)
        return __main__()
    time.sleep(default_delay)

    if(user_option == 1):
        tmp_name = input('Digite o nome do usuário a ser criado: ')
        if len(tmp_name) == 0:
            print('Digite um nome válido para criar um usuário.')   
            time.sleep(default_delay)
            return __main__()
        newPlayer(tmp_name)
        time.sleep(default_delay)
        return __main__()
    elif(user_option == 2):
        tmp_name = input('Digite o nome do usuário a ser deletado: ')
        if len(tmp_name) == 0:
            print('Digite um usuário válido para ser delatado.')   
            time.sleep(default_delay)
            return __main__()
        delPlayer(tmp_name)
        time.sleep(default_delay)
        return __main__()
    elif(user_option == 3):
        print('alguma coisa')
    elif(user_option == 4):
        time.sleep(default_delay)
        gameInit()
    elif(user_option == 5):
        os.system('cls')
        print('\n Este jogo foi desenvolvido como um trabalho para a matéria de fundamentos de algoritimos. \n Desenvolvido por Thiago Braga Martins Gomes.', end="\n")
    #gameInit()
    #_TEST_()
__main__()
