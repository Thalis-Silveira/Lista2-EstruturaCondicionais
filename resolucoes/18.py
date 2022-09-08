fileDuplo = 4.90
alcatra = 5.90
picanha = 6.90

carne = input("Digite o tipo de carne File Duplo(FD)/Alcatra(A)/Picanha(P): ").upper()
quantidade = int(input("Digite a quantidade: "))
pagamento =input("forma de pagamento Dinheiro(D)/Cartão(C): ").upper()

desconto = 0

if(carne == "FD" or carne == "A" or carne == "P"):
    if(quantidade > 5):
        fileDuplo = 5.80
        alcatra = 6.80
        picanha = 7.80
        if(carne == "FD"):
            carneEscolhida = "File Duplo"
            total = quantidade * fileDuplo
            if(pagamento == "C"):
                desconto = fileDuplo * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (fileDuplo - desconto)
            
        elif(carne == "A"):
            carneEscolhida = "Alcatra"
            total = quantidade * alcatra
            if(pagamento == "C"):
                desconto =  alcatra * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (alcatra - desconto)
            
        else:
            carneEscolhida = "Picanha"
            total = quantidade * picanha
            if(pagamento == "C"):
                desconto = picanha * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (picanha - desconto)
            
    elif(quantidade < 0):
        print("Digite valores válidos por favor!!!!")
    else:
        if(carne == "FD"):
            carneEscolhida = "File Duplo"
            total = quantidade * fileDuplo
            if(pagamento == "C"):
                desconto = fileDuplo * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (fileDuplo - desconto)
            
        elif(carne == "A"):
            carneEscolhida = "Alcatra"
            total = quantidade * alcatra
            if(pagamento == "C"):
                desconto =  alcatra * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (alcatra - desconto)
            
        else:
            carneEscolhida = "Picanha"
            total = quantidade * picanha
            if(pagamento == "C"):
                desconto = picanha * 0.05
                PagamentoRealizado = "Cartão"
            else:
                PagamentoRealizado = "Dinheiro"
            totalComDesconto = quantidade * (picanha - desconto)
            
    print("O valor final de {} com quantidade de {:.2f} Kg, será de R${:.2f}\nCom forma de pagamento: {}, sendo assim tendo desconto de R${:.2f} por Kg\nPreço final R${:.2f}".format(carneEscolhida,quantidade,total,PagamentoRealizado, desconto,totalComDesconto))
else:
    print("Tipo de carne desconhecido")

