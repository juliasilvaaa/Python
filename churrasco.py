# Desafio 2

# Organizar o churrasco
# 1 - Quantos adultos vão comparecer? 
# 2 - Quantas crianças vão participar?

print(" ----------- Planejamento para o seu churrasco ------------")
adultos = int(input("\nQuantos adultos vão comparecer? "))
criancas = int(input("Quantas crianças vão comparecer? "))


total_carne = adultos * 300 + criancas * 150
total_acompanhamentos = ( adultos + criancas) * 200
total_bebidas_alcoolicas = adultos * 2.5
total_bebidas = criancas * 1.5

print("\n ==== Para seu churrasco será necessario: ====")
print(f"-- Carne: {total_carne}")
print(f"-- Acompanhamentos: {total_acompanhamentos}")
print(f"-- Bebidas alcoolicas: {total_bebidas_alcoolicas}")
print(f"-- Refrigerantes ou Sucos: {total_bebidas} Litros")


# Com os dados em maõs, o sistema calcula
# A quantidade total de carne (300g por adulto, 150g por criança)
# A quantidade de acompanhamentos (200g por pessoa, independente da idade)
# Bebidas alcoolicas (2,5 por adulto)
# Refrigerantes ou sucos (1.5 L por criança)