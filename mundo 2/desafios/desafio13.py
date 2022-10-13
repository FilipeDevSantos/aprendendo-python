s = 0
quantidade = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        quantidade += 1
        s += c
print(f'A soma entre os {quantidade} valores é igual a {s}.')