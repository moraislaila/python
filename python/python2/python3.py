arroz = float(input("escreva seu valor"))
batata= float(input("escreva seu valor"))
suco = float(input("digite seu valor"))
valor = float(input("digite seu valor"))
soma = (batata+arroz+suco)-valor

if soma < 100:
 print(f"com troco{soma}")
else:
 print(f"sem troco{soma}")