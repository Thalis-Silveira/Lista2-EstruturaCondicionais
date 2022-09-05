a = int(input("Digite o valor de a:"))
if (a != 0):
    b = int(input("Digite o valor de b:"))
    c = int(input("Digite o valor de c:"))
    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        print("A equação não possui raizes reais")
    elif(delta == 0):
        raiz = (b * -1)/(2 * a)
        print("Possui uma raiz = {:.2f}".format(raiz))
    else:
        raizUm = ((b * -1) + delta ** 2)/( 2 * a)
        raizDois =  ((b * -1) - delta ** 2 )/( 2 * a)
        print("Possui duas raizes, sendo elas = {:.2f}, {:.2f}".format(raizUm,raizDois))
else:
    print("Não é equação do segundo grau")

