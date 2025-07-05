mes = int(input("Digite o número do mês (1 a 12): "))
meses = {
    1: ("janeiro", 31),
    2: ("fevereiro", 28), 
    3: ("março", 31),
    4: ("abril", 30),
    5: ("maio", 31),
    6: ("junho", 30),
    7: ("julho", 31),
    8: ("agosto", 31),
    9: ("setembro", 30),
    10: ("outubro", 31),
    11: ("novembro", 30),
    12: ("dezembro", 31)
}

if 1 <= mes <= 12:
    nome_mes, dias = meses[mes]
    print(f"O mês de {nome_mes} possui {dias} dias.")
else:
    print("Mês inválido. Por favor, digite um número entre 1 e 12.")
