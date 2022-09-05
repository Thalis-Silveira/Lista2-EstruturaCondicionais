saque = int(input("Valor a ser sacado R$ "))
saqueInicial = saque

if(10 <= saque <= 600):
    ntCem = saque // 100
    saque -= ntCem * 100
    ntCinquenta = saque  // 50
    saque -= ntCinquenta * 50
    ntDez = saque // 10
    saque-= ntDez * 10
    ntCinco = saque// 5
    saque -= ntCinco * 5
    ntUm = saque
    print("para sacar a quantia de {} sera usada {} de 100, {} de 50, {} de 10, {} de 5, {} de 1".format(saqueInicial,ntCem,ntCinquenta,ntDez,ntCinco,ntUm))
else:
    print("O saque apenas disponibiliza ser feito entre valores entre R$ 10 e R$ 600!\n Tente novamente mais tarde...")
    

