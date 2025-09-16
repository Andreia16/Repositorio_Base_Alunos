nome = input('Digite o nome:')
Peso = float(input('Digite o peso:'))
Altura = float(input('Digite a altura:'))
                       
imc = Peso /(Altura**2)

if  Peso < 18.5:
    print('Abaixo do peso')
          
elif Peso < 24.9:
    print('Normal')

elif Peso < 29.9:
    print('Sobrepeso')

elif Peso < 34.9:
    print('Obesidade Gral I')

elif Peso < 39.9:
    print('Obesidade Gral II')
    
else:
    print('Obesidade Gral III (Morbida)')

print(f'O imc do paciente {nome} e {imc:.2f}')

