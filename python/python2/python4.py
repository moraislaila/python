livro1 = float(input("escreva o valor"))
livro2 = float(input("escreva o valor"))
livro3 = float(input("escreva o valor"))
valor=float(input("escreva o valor"))

comDesconto = (livro1+livro2+livro3) - 15/100*valor
semDesconto = (livro1+livro2+livro3)
print(f"o seu pagamento com o desconto é {comDesconto}")
print(f"o seu pagamento sem desconto é {semDesconto}")
