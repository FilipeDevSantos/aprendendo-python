area_tecnologia = dict()
stack = list()

for c in range(0, 3):
    area_tecnologia['area'] = str(input('Qual seria a área? '))
    area_tecnologia['tecnologia'] = str(input('Qual seria a tecnologia? '))
    stack.append(area_tecnologia.copy())
for a in stack:
    for k, v in a.items():
        print(f'{k} -> {v}')