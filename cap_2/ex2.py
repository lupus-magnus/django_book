#Escreva um programa que solicita as dimensoes (largura e comprimento) de uma sala em m2, o tamanho da aresta de uma peca quadrada de ceramica em cm e o preco do metro quadrado da referida ceramica. Imprima quantos metros quadrados devem ser adquiridos para pavimentar a referida sala e descubra quanto custara a ceramica a ser usada.

dimensoes = input('Insira uma tupla (largura, comprimento), em m:\t')
azulejo = input('Tamanho da aresta do azulejo em cm:\t')
preco = input('preco do cm2 do azulejo:\t')

area = dimensoes[1]*dimensoes[0]
custo_total = area * 10**4 * preco
message = 'Precisaremos de {area} metros quadrados. O custo final sera de {custo_total} reais'.format(area=area, custo_total=custo_total)

print(message)
