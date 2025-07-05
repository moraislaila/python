ponto1= float(input("digite a pontuação: "))
ponto2= float(input("digite a pontuação: "))
ponto3= float(input("digite a pontuação: "))

SomaDosPontos = ponto1 + ponto2 + ponto3
if SomaDosPontos >= 15:
    print("Deus da peteca!")

elif SomaDosPontos >=10 and SomaDosPontos <15:
    print("petequeiro profissa!")
elif SomaDosPontos <10 and SomaDosPontos <6:
    print("petequeiro de final de semana!")
elif SomaDosPontos <5 and SomaDosPontos >0:
    print("pseudo-petequeiro!")

else:
    print("nunca petequeiro!")

print(f"a soma é:  {SomaDosPontos}")


