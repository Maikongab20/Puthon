par = 0
impar = 0

for i in range(0,10,1):
    num = int(input('digite um numero'))
    if num % 2:
        par = par + 1
        todo = todo + num
    else:
        impar = impar + 1
        todoim = todoin + num

media = todoin / impar
print('a  quatidade ded numero pares %d, e de impares %i', par,impar)
print('e a quantidade de numeros pares %d, e a media de numeros impares %i')