# Loops Aninhados em Python

# Exemplo 1: País + Estação do Ano
paises = ['Brasil', 'Canada', 'Estados Unidos', 'Australia']
estacoes_do_ano = ['Primavera', 'Verão', 'Outono', 'Inverno']

for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'No país {pais}, a estação do ano é {estacao}')
        

# Exemplo 2: Valor Externo e Interno
for valor_externo in range(1, 5):
    for valor_interno in range(1, 11):
        print(f'Valor Externo: {valor_externo} - Valor Interno: {valor_interno}')
        
