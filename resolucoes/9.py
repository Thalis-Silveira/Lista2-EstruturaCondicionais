num = int(input("Digite um número menor que  1000: "))
c = ""
d = ""
u = ""

if(num < 1000):
    c =  num // 100
    d = (num - c * 100) // 10
    u = ((c * 100 + d * 10) - num) * -1
print("O número é composto por {} centenas, {} dezenas e {} unidades".format(c, d, u))