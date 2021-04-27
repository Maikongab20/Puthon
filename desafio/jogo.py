import random
i = 1
tent = False
nome = input('digite seu nome : \n')
print('\n')
print('bem vindo ao jogo tente acertar o numero')

num=random.randint(1, 20)

while i <= 6 and tent != True:
    
    i = i + 1
    per = int(input('digite um numero : \n'))
    if num == per:
        tent = True
    else:
        print('Você errou tente de novo')
        

if tent == True:
    print('parabéns %s você é um otimo jogador' %(nome))
else:
    print('você errou o numero a ser acertado é %d '%(num))