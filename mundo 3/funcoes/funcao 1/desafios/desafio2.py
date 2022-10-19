def escrever(msg):
    size = len(msg) + 4
    print('-'*size)
    print(f'  {msg}')
    print('-'*size)


escrever('Hello, world!')
escrever('CDF')
