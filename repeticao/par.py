par = 0
impar = 0
todoimpar = 0
todopar = 0

for i in range(0,10,1):
    num = int(input('digite um numero\n'))
    if num % 2:
        par = par + 1
        todopar = todopar + num
    else:
        impar = impar + 1
        todoimpar = todoimpar + num

media = todoimpar / impar
print('a quantidade de par : %d, a quantidad de impares %d' %(par, impar))
print('a soam dos numeros pares é : %d,  e a media dos numeros impares são : %d' %(todopar, todoimpar))