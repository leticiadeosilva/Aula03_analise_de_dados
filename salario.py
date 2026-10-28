salariobruto = float(input("Digite o salário bruto: "))
if salariobruto <= 2000:
    desconto = salariobruto * 0.11
else:
    desconto = salariobruto * 0.09
salarioFinal = salariobruto - desconto

print("\n--- Demonstrativo de salário ---")
print(f"Salário bruto: R$ {salariobruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Salário final: R$ {salarioFinal:.2f}")
