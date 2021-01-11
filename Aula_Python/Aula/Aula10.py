'''
    print('Nome lindo e generico')
nome = str(input('Digite o seu nome: ')).strip().lower()
if nome == 'rodrigo':
    print('Nome Lindo esse!')
    print('Ola {}'.format(nome))
else:
    print('Nome generico voce tem!')
    print('Ola {}'.format(nome))'''




print('Media das notas')

n1 = int(input('Digite a primeira nota:'))
n2= int(input('Digite o segundo: '))
m = (n1 + n2 ) /2

print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media esta boa! Parabens')
else:
    print('Sua media esta baixa do desejado!')