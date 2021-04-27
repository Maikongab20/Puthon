import random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
jogada = 1
verd = False

print('Bem vindo a o jogo Craps ')
print('\n')
regra = input('você quer saber as regar digite S se não digite N para começar')

if regra == 'S' or 's':
    print('objetivo do kogo e regras')
    print('\n')
    print('\n')
    print('Se, na primeira jogada, você tirar 7 ou 11, você tirou um NATURAIS e ganhou.')
    print('\n')
    print('Se você tirar 2, 3 ou 12 na primeira jogada, isto e chamado de CRAPS e você perdeu.')
    print('\n')
    print('Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu PONTO. Seu objetivo agora e continuar jogando os dados até tirar este número novamente.')
    print(' Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.')

while verd != True :
    dado = dado1 + dado2

    if jogada == 1 and dado == 7:
        print('%d é um munero natural e você ganhou' %(dado))    
    elif jogada == 1 and dado == 11 :
        print('%d é um munero natural e você ganhou'%(dado))

    elif jogada == 1 and dado == 2 :
        print('Você tirou esse numero %d e isso se chama crap e você perdeu' %(dado))
        verd = True

    elif jogada == 1 and dado == 3 :
        print('Você tirro esse numero %d e isso se chama crap  e você perdeu' %(dado))
        verd = True

    elif jogada == 1 and dado == 12 :
        print('Você tirro esse numero %d e isso se chama crap  e você perdeu' %(dado))
        verd = True