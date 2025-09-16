nome = input("Digite seu nome:")
altura = float(input("Digite sua altura:")) 
peso = float(input("Digite seu peso:"))

imc = peso / (altura**2)

if  peso < 18.5:
    print('Abaixo do peso')
          
elif peso < 24.9:
    print('Normal')

elif peso < 29.9:
    print('Sobrepeso')

elif peso < 34.9:
    print('Obesidade Gral I')

elif peso < 39.9:
    print('Obesidade Gral II')
    
else:
    print("Obesidade Gral III (Morbida)")

print(f"O IMC do paciente {nome} e {imc:.2f}") 
