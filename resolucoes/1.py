salario = float(input("Digite o salário: R$"))

c = 280.00
b = 700.00
a = 1500.00

if(salario <= c):
    frac = salario  * 0.2
    salario += frac
elif( c < salario <= b):
    frac = salario  * 0.15
    salario += frac
elif( b < salario <= a):
    frac = salario * 0.1
    salario += frac
elif(salario > a):
    frac = salario * 0.05
    salario += frac
else:
    salario = "Valor invalido"
print("Reajuste = R$ {:.2f}, com o acrescimo  de R${:.2f} ".format(salario,frac))
