import math

an = float(input('Digite um angulo: '))
seno = math.sin(math.radians(an))
print('O Ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
coss = math.cos(math.radians(an))
print('O Ângulo de {} tem o Cosseno de {:.2f}'.format(an, coss))
tan = math.tan(math.radians(an))
print('O Ângulo de {} tem o Tangente de {:.2f}'.format(an, tan))