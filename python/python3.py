valor1= float(input("digite seu salario anual"))
piso = 3000
if valor1 > piso:
    print("salário mensal maior que o piso da categoria ")
elif valor1 == piso:
    print("salário mensal igual a piso de categoria")
else:
    print("salario  mensal menor que o piso")
   