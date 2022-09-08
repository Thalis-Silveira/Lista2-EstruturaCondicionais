e = input("escolha gasolina(g)|alcool(a)")
quant = int(input("Qauntos litros: "))
escolha = e.lower()
gasolina = 2.50
alcool = 1.90 

if(escolha == "a"):
    if(0 < quant <= 20):
        desc = alcool * 0.03
        alcool = alcool - desc
        total = quant * alcool 
    else:
        desc = alcool * 0.05
        alcool = alcool - desc
        total = quant * alcool 
elif(escolha == "g"):
    if(0 < quant <= 20):
        desc = gasolina * 0.04
        gasolina = gasolina - desc
        total = quant * gasolina 
    else:    
        desc = gasolina * 0.06
        gasolina = gasolina - desc
        total = quant * gasolina 
else:
    print("Forma não válida")

print("O valor total é de R${:.2f}".format(total))