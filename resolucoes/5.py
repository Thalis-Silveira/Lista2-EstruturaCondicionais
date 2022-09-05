ladoUm = int(input("Digite o tamanho do lado do triangulo:"))
ladoDois = int(input("Digite o tamanho do lado do triangulo:")) 
ladoTres = int(input("Digite o tamanho do lado do triangulo:"))

triangulo = ""

if( ladoUm + ladoDois > ladoTres or ladoUm + ladoTres > ladoDois or ladoTres + ladoDois > ladoUm):
    
    if(ladoUm == ladoDois == ladoTres):
        triangulo = "Equilátero"
    elif(ladoUm == ladoDois or ladoDois == ladoTres or ladoUm == ladoTres):
        triangulo = "Isósceles"
    else:
        triangulo = "Escaleno" 
    print("De acordo com o tamanho dos lados, constata-se que é um triângulo {}!!!".format(triangulo))
else:
    print("De acordo com o tamanho dos lados, constata-se que não é um triângulo!!!")
