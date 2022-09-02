priNota = float(input("Digite a primeira nota:"))
segNota = float(input("Digite a segunda nota:"))

media = (priNota + segNota) / 2

result = ""
conceito = ""

if(0 <= media <= 10):
    if(9 <= media <= 10):
        result = "APROVADO"
        conceito = "A"
    elif(7.5 <= media < 9):
        result = "APROVADO"
        conceito = "B"
    elif(6 <= media < 7.5):
        result = "APROVADO"
        conceito = "C"
    elif(4 <= media < 6):
        result = "REPROVADO"
        conceito = "D"
    else:
        result = "REPROVADO"
        conceito = "E"

    print("Primeira nota = {} e Segunda nota = {}\nMedia final = a {} com conceito equivalente a {}\nSendo assim você foi {}".format(priNota,segNota, media,conceito,result))
else:
    print("ERROR! reinicie o programa")   
