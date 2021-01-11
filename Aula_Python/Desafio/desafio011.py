lag = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = lag * alt 
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m2'.format(lag, alt,area))
tinta = area / 2
print('Para pintar a Parede você precisarar de {}L de tinta'.format(tinta))