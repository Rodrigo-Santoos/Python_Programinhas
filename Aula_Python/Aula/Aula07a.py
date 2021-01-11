#nome = input('Qual o seu nome? ')
#print('Prazer te conhecer {}'.format(nome))

#-----------------------------------------------------------------------------------

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
po = n1 ** n2 
print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(s,m,d), end=' ')
print('Divisao inteira {} e potencia {}'.format(di, po))