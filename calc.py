from time import sleep
while True:
    pontos = int(input('Quantos pontos você tem?: '))
    resultado = 5000-pontos
    rdetres = (10*resultado)/5
    horas = rdetres/60
    dias = horas/24

    print(f'{horas:.2f} horas, e {dias:.2f} dias')
