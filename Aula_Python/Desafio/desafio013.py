#Calculo de aumento em porcento em 15% do salario

salario = float(input('Qual o salario do funcionario? R$'))
novo = salario +(salario*15/100)
print('O funcionario que ganhava R${} ira receber R${}'.format(salario, novo))