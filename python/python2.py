nome= input("digite seu nome")
idade= int(input("digite sua idade"))
cormobidade = input("possui alguma cormobidade s ou n:")

if cormobidade == "s" or idade>=60:
 print("recebe vacina!")
else:
  print("não recebe vacina!")