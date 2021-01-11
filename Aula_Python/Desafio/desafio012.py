#Calculo de desconto em porcento em 5%


preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco*5 / 100)
print('O produto que custa R${} na promoçao de 5% vai custar R${}'.format(preco, novo))