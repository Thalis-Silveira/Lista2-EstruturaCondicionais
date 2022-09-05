nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))

media = (nota1 + nota2 + nota3)/3

if(0 <= media <= 10):
    if(media == 10):
        print("Aprovado com Distinção")
    elif(media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("ERROR")