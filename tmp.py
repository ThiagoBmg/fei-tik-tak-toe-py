# FUNÇÃO DE TESTES 
def _TEST_():
	#adicionando novo player para testar função
    MOCK_USER = "UserTestThiagoFeiOPaiEstaOnlineCondandoMuito"

    print("Testando função que desenha o tabuleiro 🧪 " ,end="\n")
    printGame()
    newPlayer(MOCK_USER)
    print("Usuário Teste Criado com Sucesso 🧪 ", end="\n")
    #Tentando criar o mesmo usuário duas vezes    
    newPlayer(MOCK_USER)
    
    # tentando encontrar o usuário de test
    searchPlayer("Thiago")

    matriz[4][4] = "x"
    printGame()
    ## tentando deletar um usuário que não existe
    #delPlayer("testUser")
    ## deletando o usuário de testes
    #delPlayer(MOCK_USER)
    #print("Usuário de teste Deletado com Sucesso 🧪 ",end="\n"
""" 
doSomething("x",2,2)
print(actions)
time.sleep(1)
doSomething("o",4,2)
print(actions)
time.sleep(2)
doSomething("x",3,2)
print(actions)
time.sleep(2)
doSomething("o",4,1)
print(actions)
time.sleep(2)
doSomething("x",3,2)
print(actions)
time.sleep(2)
doSomething("x",3,1)
print(actions)
time.sleep(2)
doSomething("o",4,2)
print(actions)
time.sleep(2) """
