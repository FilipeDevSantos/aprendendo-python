import requests


try:
    site = requests.get('http://www.pudim.com.br')
except:
    print('\033[31mProblemas ao tentar acessar o site, por favor verifique sua conexão a internet!\033[m')
else:
    print('\033[33mConsegui acessar o site do pudim! :)\033[m')
finally:
    print('\033[32mPrograma finalizado!\033[m')