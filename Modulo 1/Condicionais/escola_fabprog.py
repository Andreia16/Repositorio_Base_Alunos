nome_aluno = input('Digite o nome:')
nota_1= float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
nota_3 = float(input(' Digite a terceira nota:'))

media =( nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print('Aprovado')

elif media >=4:
    print('Esta na media')
    
else:
    print('Reprovado')

print(f'A media do aluno {nome_aluno} e {media :.1f}')



