from multiprocessing.resource_sharer import stop


morango = 2.50
maca = 1.80

quantMorango = float(input("Escreva a quantidade comprada de de Morangos em Kg: "))
quantMaca = float(input("Escreva a quantidade comprada de de Maçãs em Kg: "))

desconto = 0

total = quantMaca * maca + quantMorango * morango 

if(quantMaca + quantMorango > 5):
    morango = 2.20
    maca = 1.50
    if(quantMaca + quantMorango > 8 or total > 25):
        desconto = total * 0.1
        total = total - desconto
    print("O valor total comprado ao final é de R${:.2f} reais".format(total))
elif(quantMaca < 0 or quantMorango < 0):
    print("Digite valores válidos por favor!!!!")
else:
    print("O valor total comprado ao final é de R${:.2f} reais".format(total))

