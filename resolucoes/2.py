salarioPoHora = float(input("Digite o seu sálario por hora: R$"))
horasTrabalhadas = int(input("Digite o número de horas trabalhadas: "))

salarioBruto = salarioPoHora * horasTrabalhadas
i = 10
inss = salarioBruto * 0.1

f=11
fgts =  salarioBruto * 0.11
sindicato = salarioBruto * 0.03


if(salarioBruto < 900):
    p = 0
    ir = 0
    salarioLiquido = (salarioBruto - ir)  - inss
elif(salarioBruto <= 1500):
    p = 5
    ir = salarioBruto * 0.05
    salarioLiquido = (salarioBruto - ir)  - inss
elif(salarioBruto <= 2500):
    p = 10
    ir = salarioBruto * 0.1
    salarioLiquido = (salarioBruto - ir)  - inss
elif(salarioBruto > 2500):
    p = 20 
    ir = salarioBruto * 0.2
    salarioLiquido = (salarioBruto - ir) - inss
else: 
    print("Salário inválido, reinicie o programa!!!")

totalDescontos = ir  + inss
    
print("Salário bruto: ({:.2f} * {:.2f})           :R$ {:.2f}\n".format(salarioPoHora,horasTrabalhadas,salarioBruto) + 
    "   (-) IR   ({}%)                         :R$ {:.2f}\n".format(p,ir) + 
    "   (-) INSS ({}%)                        :R$ {:.2f}\n".format(i,inss) + 
    "       FGTS ({}%)                        :R$ {:.2f}\n".format(f,fgts) + 
    "       Total de descontos                :R$ {:.2f}\n".format(totalDescontos) + 
    "       Salário Liquido                   :R$ {:.2f}".format(salarioLiquido))