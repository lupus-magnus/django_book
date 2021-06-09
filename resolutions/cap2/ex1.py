#Crie um programa que receba cinco numeros inteiros e os imprima na ordem inversa em que foram digitados.

num_1 = input('Coloque seu numero #1:\t')
num_2 = input('Coloque seu numero #2:\t')
num_3 = input('Coloque seu numero #3:\t')
num_4 = input('Coloque seu numero #4:\t')
num_5 = input('Coloque seu numero #5:\t')

my_list = [num_1, num_2, num_3, num_4, num_5]
my_list.reverse()

print(my_list)