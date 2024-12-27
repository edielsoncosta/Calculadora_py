# lista salarios guardando valores

salarios = [1000, 5000, 7000, 850]

# funcao aumentar_salarios com condições, se salário maior de 3 mil, a porcentagem de aumento é menor do que de quem ganha menos de 3mil

def aumentar_salarios(salario):
    if salario > 3000:
        novo_salario = salario * 1.08
    
    else:
        novo_salario = salario * 1.1
    return novo_salario

# pegando a function e a list e jogando na map, salarios sendo requisito para funcionamento da function

novos_salarios = list(map(aumentar_salarios, salarios))
print(novos_salarios)


# pegando a list e dando um filter em salários maiores de 2 mil, pegando os valores da list na lambda x e jogando os valores true
# dentro da variável salarios_altos

# por ter o list, a variável salarios_altos também vira uma list
salarios_altos = list(filter(lambda x: x > 2000, salarios))
print(salarios_altos)


# lista custos

custos = [600, 5000, 500, 4250]


# começando a contabilizar os custos com o valor fixo mil, gerando um valor mil a mais na conta

custo_total = sum(custos, start=1000)
print(custo_total)



salarios2 = [1000, 5000, 7000, 850]

# retorna os valores ordenados, de forma aumentativa
salarios_ordenados = sorted(salarios2)
print(salarios_ordenados)

# retorna os valores ordenados, de forma diminutiva
salarios_ordenados2 = sorted(salarios2, reverse=True)
print(salarios_ordenados2)


# lista com 4 funcionários, sendo ordenados por salario, bonificação e vale alimentação

salarios3 = [
    (1000, 500, 180),
    (5000, 40, 200),
    (7000, 0, 0),
    (600, 100, 150),
]

# ordenando a lista salarios3, do maior para o menor, pela soma total de todos os seus beneficios
funcionarios_ordenados = sorted(salarios3, reverse=True, key=lambda x: sum(x))
print(funcionarios_ordenados)

funcionarios_ordenados = sorted(salarios3, reverse=False, key=lambda x: x[1])
print(funcionarios_ordenados)
