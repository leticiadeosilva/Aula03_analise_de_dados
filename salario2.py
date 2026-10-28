salarioBruto = float(input("Salário: ").replace (",","."))
if salarioBruto >=2000:
    desconto = salarioBruto *0.11
else:
    desconto = salarioBruto *0.09
salarioFinal = salarioBruto - desconto
print(f"Salario: {salarioBruto:.2f}")
print(f"Desconto: {desconto: .2f}")
print(f"Salario Final: {salarioFinal: .2f}")
