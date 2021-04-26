sim = 0
nao = 0 
iden = 0
pesso = 0
simF = 0
naoM = 0
print('Voce que particiar da pesquisa da empresa Cara de Pau Ltda')
pesq = int(input('digite 9 para particiar e 0 para não : \n'))

while pesq != 0 :
    
    sexo = str(input('digite o seu sexo M para homen e f para feminino: \n'))

    idade = int(input('digite a sua idade: \n'))

    print('\n')

    print('digite as resposta assim :')
    print('S para sim')
    print('N para não')
    print('I para indiferente')

    print('\n')

    per = str(input('Voce ficou satidfeito com a jogabilidade do jogo: \n'))
    if(per == 's' or per == 'S'):
        sim = sim + 1
    elif(per == 'n' or per == 'N'):
        nao = nao + 1
    elif(per == 'i' or per == 'I'):
        iden = iden + 1
    print('\n')
   
    per = str(input('Os graficos do jogo são bons : \n'))
    if(per == 's' or per == 'S'):
        sim = sim + 1
    if(per == 'n' or per == 'N'):
        nao = nao + 1
    if(per == 'i' or per == 'I'):
        iden = iden + 1
    print('\n')

    per = str(input('Os comandos do jogo são difíceis : \n'))
    if(per == 's' or per == 'S'):
        sim = sim + 1
    if(per == 'n' or per == 'N'):
        nao = nao + 1
    if(per == 'i' or per == 'I'):
        iden = iden + 1
    print('\n')

    per = str(input('Voce recomendaria o nosso joga para um amigo : \n'))
    if(per == 's' or per == 'S'):
        sim = sim + 1
    if(per == 'n' or per == 'N'):
        nao = nao + 1
    if(per == 'i' or per == 'I'):
        iden = iden + 1
    print('\n')

    if sexo == 'f' or sexo == 'F':
        simF = simF + 1
    else:
        naoM = naoM + 1

    pesso = pesso + 1
    percent = nao/100

print('A quantidadde de pessoas que foram intrevistadas foram : %d' %(pesso))
print('\n')
print('quantidades de sim de cada pergunta foi : %d' %(sim))
print('\n')
print(', e a quantidade de pessoas que disseram não foi : %d' %(nao))
print('\n')
print('O percentual de pessoas que responderam Não : %d \n')
print('\n')
print('A quantidadde de mulheres que disseram sim : %d' %(simF))
print('\n')
print('A quantidadde de homens que respoderam não : %d' %(naoM))