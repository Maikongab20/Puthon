gabarito = ['a', 'c', 'b', 'd', 'e', 'b', 'c', 'a','d','e']
ponto = 0 
resposta = []

i = input('ver resposta da prova digite 0 oara sair \n')

while i != 0:
 
    for j in range(0,10,1):
        
        print('digite as resposta a, b, c, d, e')
        print('\n')
        print('Pergunta numero %d' %(j))
        respo = input('digite a resposta \n')
        resposta.append(respo)
        print('\n')
    for j in range(0,10,1):

        if(gabarito[j] == resposta[j]):
            ponto = ponto + 1
        
    print('\n')
    print('\n')
    print('você arcertou %d perguntas' %(ponto))
    print('\n')
    resposta = []
    i = input('ver resposta da prova digite 0 para sair\n')
