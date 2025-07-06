num1 = int(input("digite seu numero"))

if num1 % 2 == 0 and num1 < 0:
    print(f"valor{num1}é par e negativo")

elif num1 % 2 == 0 and num1 > 0:
    print(f"valor {num1}é par e positivo")

elif num1 % 2 == 1 and num1 <0:
    print(f"valor {num1} impar e negativo")

else:
    print(f"valor {num1} é impar e positivo") 