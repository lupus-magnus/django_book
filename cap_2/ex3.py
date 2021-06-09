#Crie um programa que entre como input a cotacao do dolar e uma quantidade em reais para converter e de a saida em dolares.

cotacao = input('Valor do dolar hoje:\t')
valor_reais = input('Quantos reais voce quer converter:\t')

resultado = (float(valor_reais) / float(cotacao))

print("Seu valor convertido e %.2f dolares" % resultado)