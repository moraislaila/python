nome1 = input("digite seu nome")
idade1= int(input("digite sua idade"))
nome2 = input("digite seu nome")
idade2 =int (input("digite sua idade"))
nome3= input("digite seu nome")
idade3= int(input("digite sua idade"))

media=(idade1+idade2+idade3)/3
 
if idade1 > idade2 and idade1>idade3:
    print("idade um é maior")

elif idade2 > idade1 and idade2 > idade3:
    print("idade dois é maior")

else:
    print("idade tres é maior")

    print(f"a média é: {media}")
