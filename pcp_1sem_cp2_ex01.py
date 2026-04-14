estado = int(input("Qual o estado de origem da carga? (entre 1 e 5) : "))
peso_toneladas = float(input("Qual é o peso da carga do caminhao - em toneladas? : "))
codigo = int(input("Qual o código da carga?(entre 10 e 40) : "))

#converter toneladas para quilos
peso_kg = peso_toneladas * 1000

#definir preço por quilo
if 10 <= codigo <= 20:
    preco_kg = 100.0
elif 21<= codigo <= 30:
    preco_kg = 250.0
else:
    preco_kg = 340.0

#preço da carga
preco_carga = preco_kg * peso_kg

#imposto
if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
else:
    imposto = 0

valor_imposto = preco_carga * imposto

#resultado final

total = preco_carga + valor_imposto

print(input(f"O peso convertido para quilos é de : {peso_kg} (enter para continuar)") )
print(input(f"O valor da carga é de : {preco_carga} (enter para continuar) "))
print(input(f"O valor que será pago de imposto é de: {valor_imposto} (enter para continuar) "))
print(input(f"O valor total transportado pelo caminhão é de : {total}"))