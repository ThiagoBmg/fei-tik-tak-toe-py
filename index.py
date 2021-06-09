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
players=[]

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
# função que busca o histórico do jogador
def getHistory(username):
    d_u_name = username.upper() # transformando em caixa alta antes de buscar o arquivo
    if os.path.isfile("./{}.txt".format(d_u_name)):
        file_tmp = open("./{}.txt".format(d_u_name)) # lendo numero de vitórias e derrotas do usuário encontrado anteriormente
        file = file_tmp.readlines() # lendo as linhas
        print("Usuário {}, atualmente esta com {} vitórias e {} derrotas 🎉 ".format(username,file[0].replace('\n',''), file[1].replace('\n','')) , end="\n")
        file_tmp.close() # fechando arquivo
        input('Digite enter para retornar ao menu ⌨ ')
        time.sleep(default_delay)
        __main__()
    else:
        print("Usuário não encontrado, tente novamente 😓",  end="\n")
        time.sleep(default_delay*2)
        return __main__()
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
# função que incrementa o ponto ou derrota para os jogadores
def incrementValue(value):
    global players
    #print(players[0].upper())
    tmp1 = open('./{}.txt'.format(players[0].upper()), "r")
    tmp2 = open('./{}.txt'.format(players[1].upper()), "r")
    tmp1l = tmp1.readlines() 
    #print(tmp1l)
    tmp1l = [int(tmp1l[0].replace('\n','')),int(tmp1l[1].replace('\n',''))]
    tmp2l = tmp2.readlines()
    tmp2l = [int(tmp2l[0].replace('\n','')),int(tmp2l[1].replace('\n',''))]
    tmp1.close()
    tmp2.close()

    if value == "X":
        tmp1l = [tmp1l[0]+1, tmp1l[1]]
        tmp2l = [tmp2l[0], tmp2l[1]+1]
        
    else:
        tmp1l = [tmp1l[0]+1, tmp1l[1]]
        tmp2l = [tmp2l[0], tmp2l[1]+1]
    
    new_file = open("./{}.txt".format(players[0].upper()), "w")
    new_file.write("{}\n".format(tmp1l[0]))
    new_file.write("{}\n".format(tmp1l[1]))
    new_file.close() # fechando arquivo

    new_file = open("./{}.txt".format(players[1].upper()), "w")
    new_file.write("{}\n".format(tmp2l[0]))
    new_file.write("{}\n".format(tmp2l[1]))
    new_file.close() # fechando arquivo
    #print(tmp1l)
# função responsável por validar o status do jogo. interar a quantidade de jogadas . validar se algum dos usuários venceu a partida
def handlerV():
    global game_status
    global actions
    actions +=1
    printGame()
    if (matriz[0][0]=="X" and matriz[0][1]=="X" and matriz[0][2]=="X" and matriz[0][3]=="X") or (matriz[0][1]=="X" and matriz[0][2]=="X" and matriz[0][3]=="X" and matriz[0][4]=="X")  or (matriz[1][0]=="X" and matriz[1][1]=="X" and matriz[1][2]=="X" and matriz[1][3]=="X") or (matriz[1][1]=="X" and matriz[1][2]=="X" and matriz[1][3]=="X" and matriz[1][4]=="X") or (matriz[2][0]=="X" and matriz[2][1]=="X" and matriz[2][2]=="X" and matriz[2][3]=="X") or (matriz[2][1]=="X" and matriz[2][2]=="X" and matriz[2][3]=="X" and matriz[2][4]=="X") or (matriz[3][0]=="X" and matriz[3][1]=="X" and matriz[3][2]=="X" and matriz[3][3]=="X") or (matriz[3][1]=="X" and matriz[3][2]=="X" and matriz[3][3]=="X" and matriz[3][4]=="X") or (matriz[4][0]=="X" and matriz[4][1]=="X" and matriz[4][2]=="X" and matriz[4][3]=="X") or (matriz[4][1]=="X" and matriz[4][2]=="X" and matriz[4][3]=="X" and matriz[4][4]=="X") or (matriz[0][0]=="X" and matriz[1][0]=="X" and matriz[2][0]=="X" and matriz[3][0]=="X") or (matriz[1][0]=="X" and matriz[2][0]=="X" and matriz[3][0]=="X" and matriz[4][0]=="X") or (matriz[0][1]=="X" and matriz[1][1]=="X" and matriz[2][1]=="X" and matriz[3][1]=="X") or (matriz[1][1]=="X" and matriz[2][1]=="X" and matriz[3][1]=="X" and matriz[4][1]=="X") or (matriz[0][2]=="X" and matriz[1][2]=="X" and matriz[2][2]=="X" and matriz[3][2]=="X") or (matriz[1][2]=="X" and matriz[2][2]=="X" and matriz[3][2]=="X" and matriz[4][2]=="X") or (matriz[0][3]=="X" and matriz[1][3]=="X" and matriz[2][3]=="X" and matriz[3][3]=="X") or (matriz[1][3]=="X" and matriz[2][3]=="X" and matriz[3][3]=="X" and matriz[4][3]=="X") or (matriz[0][4]=="X" and matriz[1][4]=="X" and matriz[2][4]=="X" and matriz[3][4]=="X") or (matriz[1][4]=="X" and matriz[2][4]=="X" and matriz[3][4]=="X" and matriz[4][4]=="X") or (matriz[0][0]=="X" and matriz[1][1]=="X" and matriz[2][2]=="X" and matriz[3][3]=="X") or (matriz[1][1]=="X" and matriz[2][2]=="X" and matriz[3][3]=="X" and matriz[4][4]=="X") or (matriz[0][4]=="X" and matriz[1][3]=="X" and matriz[2][2]=="X" and matriz[3][1]=="X") or (matriz[4][0]=="X" and matriz[3][1]=="X" and matriz[2][2]=="X" and matriz[1][3]=="X"):
        incrementValue('X')
        print("🎉 🥳 🏆  vitória jogador X 🏆  🥳  🎉 ") 
        game_status = False
    elif(matriz[0][0]=="O" and matriz[0][1]=="O" and matriz[0][2]=="O" and matriz[0][3]=="O") or (matriz[0][1]=="O" and matriz[0][2]=="O" and matriz[0][3]=="O" and matriz[0][4]=="O") or (matriz[1][0]=="O" and matriz[1][1]=="O" and matriz[1][2]=="O" and matriz[1][3]=="O") or (matriz[1][1]=="O" and matriz[1][2]=="O" and matriz[1][3]=="O" and matriz[1][4]=="O") or (matriz[2][0]=="O" and matriz[2][1]=="O" and matriz[2][2]=="O" and matriz[2][3]=="O") or (matriz[2][1]=="O" and matriz[2][2]=="O" and matriz[2][3]=="O" and matriz[2][4]=="O") or (matriz[3][0]=="O" and matriz[3][1]=="O" and matriz[3][2]=="O" and matriz[3][3]=="O") or (matriz[3][1]=="O" and matriz[3][2]=="O" and matriz[3][3]=="O" and matriz[3][4]=="O") or (matriz[4][0]=="O" and matriz[4][1]=="O" and matriz[4][2]=="O" and matriz[4][3]=="O") or (matriz[4][1]=="O" and matriz[4][2]=="O" and matriz[4][3]=="O" and matriz[4][4]=="O") or (matriz[0][0]=="O" and matriz[1][0]=="O" and matriz[2][0]=="O" and matriz[3][0]=="O") or (matriz[1][0]=="O" and matriz[2][0]=="O" and matriz[3][0]=="O" and matriz[4][0]=="O") or (matriz[0][1]=="O" and matriz[1][1]=="O" and matriz[2][1]=="O" and matriz[3][1]=="O") or (matriz[1][1]=="O" and matriz[2][1]=="O" and matriz[3][1]=="O" and matriz[4][1]=="O") or (matriz[0][2]=="O" and matriz[1][2]=="O" and matriz[2][2]=="O" and matriz[3][2]=="O") or (matriz[1][2]=="O" and matriz[2][2]=="O" and matriz[3][2]=="O" and matriz[4][2]=="O") or (matriz[0][3]=="O" and matriz[1][3]=="O" and matriz[2][3]=="O" and matriz[3][3]=="O") or (matriz[1][3]=="O" and matriz[2][3]=="O" and matriz[3][3]=="O" and matriz[4][3]=="O") or (matriz[0][4]=="O" and matriz[1][4]=="O" and matriz[2][4]=="O" and matriz[3][4]=="O") or (matriz[1][4]=="O" and matriz[2][4]=="O" and matriz[3][4]=="O" and matriz[4][4]=="O") or (matriz[0][0]=="O" and matriz[1][1]=="O" and matriz[2][2]=="O" and matriz[3][3]=="O") or (matriz[1][1]=="O" and matriz[2][2]=="O" and matriz[3][3]=="O" and matriz[4][4]=="O") or (matriz[0][4]=="O" and matriz[1][3]=="O" and matriz[2][2]=="O" and matriz[3][1]=="O") or (matriz[4][0]=="O" and matriz[3][1]=="O" and matriz[2][2]=="O" and matriz[1][3]=="O"):
        incrementValue('O')    
        print("🎉 🥳  🏆  vitória jogador O  🏆 🥳  🎉 ")
        game_status = False
    elif actions >= 26:
        print("🤦 🤦 EMPATE 🤦 🤦")
        game_status = False
        

# função que reserva o espaço na matriz caso ele esteja livre
def doSomething(user, linha , coluna):
    if matriz[linha][coluna] != " ":
        printGame()
        print("⚠ Esta posição já foi reservada anteriormente. Escolha outra posição ⚠")  
    else:
        matriz[linha][coluna] = user
        handlerV()
# função que inicia o jogo
def gameInit():
    global game_status
    global players
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
        return __main__()
    else:
	    game_status = True
        
    players = [first_player,second_player]    
    printGame()
    #print(players)
    # iniciando o game depois de realizar as validações a cima
    while game_status:
        #print('Number of actions: '+ str(actions))
        #print('result of operation: '+str(int(actions%2)))
        ob = ''
        # validando se o numero de ações é par, caso seja, sera vez do player X, se for impar, vez do player O
        if actions == 0 or actions%2 == 0:
            ob = 'X'
        else: 
            ob = 'O'
        # realizando jogada
        try:
            lin = int(input("Digite qual a linha para o usuário [{}]: ".format(ob)))
            col = int(input("Digite qual a coluna para o usuário [{}]: ".format(ob)))

            if lin < 0 or lin > 5 or col < 0 and col > 5:
                printGame()
                print("⚠ Digite um valor válido para realizar sua jogada ⚠",end="\n")
                print("⚠ O valor que deve ser levado em consideração é um número inteiro entre 1-5 ⚠",end="\n")
            else:    
                doSomething(ob, lin-1, col-1)
        except Exception:
            printGame()
            print("⚠ Digite um valor válido para realizar sua jogada ⚠",end="\n")
            print("⚠ O valor que deve ser levado em consideração é um número inteiro entre 1-5 ⚠",end="\n")
        
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

    user_option = '' 
    try:
        user_option = int(input("-"*5+" Digite uma das opções: "))
    except Exception:
        print("Ops! parece que esta não é uma opção válida, tente novamente 😓",  end="\n")
        print(Exception.__str__)
        time.sleep(default_delay*2)
        return __main__()

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
        tmp_name = input('Digite o nome do usuário que deseja buscar: ')
        if len(tmp_name) == 0:
            print('Digite um usuário válido para realizar a busca 😓')   
            time.sleep(default_delay)
            return __main__()
        return getHistory(tmp_name)
    elif(user_option == 4):
        gameInit()
    elif(user_option == 5):
        os.system('cls')
        print('\n Este jogo foi desenvolvido como um trabalho para a matéria de fundamentos de algoritimos. \n Desenvolvido por Thiago Braga Martins Gomes.', end="\n")

__main__()
""" players=['thiago','renan']
doSomething('X',0,0)
time.sleep(1)
doSomething('X',1,1)
time.sleep(1)
doSomething('X',2,2)
time.sleep(1)
doSomething('X',3,3)
 """
#doSomething('O',2,2)
#time.sleep(1)
#doSomething('O',3,3)
#time.sleep(1)
#doSomething('O',4,4)
#time.sleep(1)
#doSomething('O',1,1)
#time.sleep(1)