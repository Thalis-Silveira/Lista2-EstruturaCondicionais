print('''Telefonou para a vítima?\n
Esteve no local do crime?\n
Mora perto da vítima?\n
Devia para a vítima?\n
Já trabalhou com a vítima?\n''')

quant = int(input("Digite o número de perguntas que se constatam como verdade: "))

if(quant == 2):
    print("A pessoa é considerada Suspeita")
elif(3 <= quant < 5):
    print("A pessoa é considerada Cúmplice")    
elif(quant == 5):
    print("A pessoa é considerada Culpada")
elif( 5 < quant < 0):
    print("o número precisa ser entre 0 e 5")
else:
    print("A pessoa é considerada Inocente")
