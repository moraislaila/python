altura =float(input("digite sua altura atual "))
peso = float(input("digite seu peso atual"))
 
IMC = peso/(altura*altura)

if IMC <=18:
 print(f"abaixo do peso {IMC}")

elif IMC >18 and IMC < 25:
  print(f"está de acordo com o peso {IMC}")

else:
   print(f"está acima do peso {IMC}") 