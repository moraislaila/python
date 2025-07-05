valor1= int(input("digite seu primeiro numero"))
valor2= int(input("digite seu segundo numero"))
valor3 = int(input("digite seu terceiro numero"))
media = (valor1+valor2+valor3)/3

if media>=7:
 print(f"aprovado,parabens você alcançou media de {media}")
else:
 print(f"reprovado,você não alcançou o necessário pra passar, sua media foi de {media}")