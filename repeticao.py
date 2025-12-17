# A estrutura de repetição 'for' em Python é usada para iterar sobre uma sequência 
# (como uma lista, tupla, dicionário, conjunto ou string) ou um intervalo de números.
# Excelente para utilizarmos quando sabemos o número exato de iterações, evitando assim, linhas de códigos desnecessárias.

# Exemplo 1: Printando uma sequência de números de 0 a 10
for numero in range(11): # o último número não é incluído, então para incluir o 10, usamos 11
    print('Número:', numero)
    

# Exemplo 2: Incluindo os steps (passos) na repetição
print('Números pares de 0 a 20:')
for numeros in range(0, 21, 2): # o primeiro número é o início, o segundo é o fim (não incluído) e o terceiro é o passo
    print(numeros)
    
# Exemplo 3: Iterando sobre uma lista de nomes
nomes = ['Ana', 'Bruno', 'João', 'Maria']
for nome in nomes:
    print(nome)