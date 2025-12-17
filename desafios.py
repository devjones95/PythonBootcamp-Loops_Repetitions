'''
Desafio 1
Usando um loop, exiba na tela: Estamos em X, onde X é um valor iniciando em 18 e finalizando em 110. 
'''
for x in range(18, 111):
    print(f'Estamos em {x}')
    
    
'''
Desafio 2
Precisamos de 10 passos para finalizar uma tarefa. 
Exiba na tela, usando um loop for, a seguinte frase: "Realizando o Passo X"
'''
for passo in range(1, 11):
    print(f'Realizando o Passo {passo}')

'''
Desafio 3
Imprima na tela a marca + celular de todos os celuliares, usando as informações abaixo:
'''
marcas = ['Samsung', 'Apple', 'Xiaomi', 'Motorola', 'ASUS']
versoes = ['Lite', 'Plus', 'Pro', 'Max', 'Ultra']

for marca in marcas:
    for versao in versoes:
        print(f'Marca: {marca} - Versão: {versao}')