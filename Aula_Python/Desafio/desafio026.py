f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(f.find('A')+1))
print('A ultima posiçao da letra A esta {}'.format(f.rfind('A')+1))