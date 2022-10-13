n = int(input('Digite quantos elementos deseja ver: '))
e = t = 0
p = 1

c = 0
while c < n:
    print(f'{e} -> ', end='')
    t = p
    p += e
    e = t
    c += 1
print('FIM')