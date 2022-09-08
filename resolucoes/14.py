num =  float(input("Digite o numero1:"))
num2 = float(input("Digite o numero2:"))

o = input("###########Digite a operação desejada###########\nPar ou Ímpar(j)\nPositivo ou negativo(k)\nInteiro ou Decimal(l)\n")
operacao = o.lower()
if(operacao == "j"):
    if(num % 2 != 0 and num2 % 2 != 0):
        print("O numero {} é ímpar e o numero {} é ímpar".format(num,num2))
    elif(num % 2 != 0 and num2 % 2 == 0):
        print("O numero {} é ímpar e o numero {} é par".format(num,num2))
    elif(num % 2 == 0 and num2 % 2 != 0):
        print("O numero {} é par e o numero {} é ímpar".format(num,num2))
    else:
        print("O numero {} é par e o numero {} é par".format(num,num2))
elif(operacao == "k"):
    if(num > 0 and num2 > 0):
        print("O numero {} positivo e o numero {} positivo".format(num,num2))
    elif(num > 0 and num2 < 0):
        print("O numero {} positivo e o numero {} é negativo".format(num,num2))
    elif(num < 0 and num2 > 0):
        print("O numero {} é negativo e o numero {} positivo".format(num,num2))
    else:
        print("O numero {} é negativo e o numero {} é negativo".format(num,num2))
elif(operacao == "l"):
    if(num - int(num) != 0 and num2 - int(num) != 0):
        print("O numero {} é decimal e o numero {} é decimal".format(num,num2))
    elif(num - int(num) == 0 and num2 - int(num) != 0):
        print("O numero {} é inteiro e o numero {} é decimal".format(num,num2))
    elif(num - int(num) != 0 and num2 - int(num) == 0):
        print("O numero {} é decimal e o numero {} é inteiro".format(num,num2))
    else:
        print("O numero {} é inteiro e o numero {} é inteiro".format(num,num2))
else:
    print("Operação não reconhecida")