maior = 0
menor = 99999

print('digite zero para sair da repetição')

num = int(input('digite um numero \n'))

while num != 0 :
    
    if num < 0:
        print('numero invalido digite outro')

    if num == 0:
        print('finalisada a repetição')
    
    elif num < menor :
        menor = num
    elif num > maior :
        maior = num
    
    num = int(input('digite um numero \n'))

print('o maior numero é %d, e o menor munero %d' %(maior, menor))