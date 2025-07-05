nome = input("digite seu username")
senha = input("digite seu passaword")

if senha == "123" and nome == "adimin":
 print("login efetuado")

elif senha != "123":
   print("passaword errada")

elif nome != "adimin":
   print("username errado")
  
else :
  print("login falhou ")