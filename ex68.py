
from random import randint
nome = 'PAR OU ÍMPAR'
print('='*30)
print(f'{nome:^30}')
print('='*30)
vitoria = 0
while True:
    usuario = int(input('Diga um valor: '))
    opcao = str(input('Você deseja PAR ou ÍMPAR(P/I): ')).upper()
    while opcao not in ('P','I'):
        opcao = str(input('DIGITE NOVAMENTE(P/I): ')).upper()    
    print('='*30)
    computador = randint(1, 10)
    print(f'Você jogou {usuario} e o computador {computador}')
    soma = usuario + computador
    if soma % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    if result == opcao:
        print('VOCÊ GANHOU!')
        vitoria += 1
        print('='*30)
    else: 
        print('VOCÊ PERDEU!')
        print('='*30)
        break
print(f'Seu total de vitórias consecutvas foram {vitoria}')
print('='*30)