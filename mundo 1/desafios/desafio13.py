preco = float(input('Qual é o preço do produto? '))

desconto = (preco * 5) / 100
valor_final = preco - desconto

print(f'O produto com o desconto fica por R$ {valor_final}.')