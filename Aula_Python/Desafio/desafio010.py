n = float(input('Quantos reais você tem ? R$'))
dl = n / 5.31
EU = n / 6.37
IE = n / 0.051
print('Com R${} Reais você pode comprar US${:.2f} Dolares, EU${:.2f} Euros e 1¥ {:.2f} Ienes '.format(n,dl, EU, IE))