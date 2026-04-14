# exercicio 4 cp2
nome = input("Digite seu nome: ")

# 🔹 validação do cargo
while True:
    cargo = int(input("Digite seu cargo (1- gerente, 2 - analista, 3 - assistente, 4 - estagiario): "))
    if cargo == 1 or cargo == 2 or cargo == 3 or cargo == 4:
        print('cargo validado')
        break
    else:
        print('resposta incorreta')


salario_base = float(input('Digite seu salario: '))
horas_extras = float(input('Digite a quantidade de horas extras: '))
faltas = int(input('Digite o total de faltas do mes: '))


# 🔹 validação do bônus (s/n)
while True:
    bonus_por_desempenho = input('Recebeu bonus por desempenho(s/n): ').lower()
    if bonus_por_desempenho == 's' or bonus_por_desempenho == 'n':
        break
    else:
        print('resposta incorreta')


def calc_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas


def calc_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas


def calc_bonus(cargo, recebeu_bonus):
    bonus = 0

    if recebeu_bonus == 's':
        if cargo == 1:
            bonus = 1000
        elif cargo == 2:
            bonus = 500
        elif cargo == 3:
            bonus = 300
        elif cargo == 4:
            bonus = 100

    return bonus


valor_horas_extras = calc_horas_extras(salario_base, horas_extras)
valor_descontos = calc_descontos_faltas(salario_base, faltas)
valor_bonus = calc_bonus(cargo, bonus_por_desempenho)

salario_bruto = salario_base
total_acrescimos = valor_horas_extras + valor_bonus
salario_final = salario_bruto + total_acrescimos - valor_descontos


print("\n--- RESULTADO ---")
print(f"Nome: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de descontos: R$ {valor_descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")