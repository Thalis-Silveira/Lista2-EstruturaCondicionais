dia,mes,ano = input("Digite uma data(dd/mm/aaaa): ").split("/")

d = int(dia)
m = int(mes)
a = int(ano)
val = ""

if(0 <= a <= 9999 and 0 < m <= 12):
    if((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and 0 < d <= 31):
        val = "Válido"
    elif(m == 2 and 0 < d <= 28):
        val = "Válido"
    elif((m == 4 or m == 6 or m == 9 or m == 11) and 0 < d < 31):
        val = "Válido"
    else:
        val = "Inválido"    
else:
    val = "Inválido"

print("A data {}/{}/{} é {}".format(d,m,a,val))
