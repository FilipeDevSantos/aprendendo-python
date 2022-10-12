altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}.')
if imc < 18.5:
    print('faixa de peso: Abaixo do Peso.')
elif imc >= 18.5 and imc < 25:
    print('Faixa de peso: Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('Faixa de peso: Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Faixa de peso: Obesidade.')
else:
    print('Faixa de peso: Obesidade Mórbida.')