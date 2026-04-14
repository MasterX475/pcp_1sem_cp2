nome_cliente = input("Digite seu nome: ")
idade_cliente = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
emprestimo_desejado = float(input("Digito o empréstimo desejado: "))
num_parcelas = int(input("Digite a quantidade de parcelas (3 a 24 parcelas): "))



def pode_aprovar(idade, renda, valor):
    if idade < 18:
        print("Empréstimo reprovado")
        return False

    elif valor > renda*20:
        print("Empréstimo reprovado")
        return False

    else:
        print("Empréstimo aprovado")
        return True

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 5/100

    elif parcelas <= 12:
        return 8/100

    else:
        return 10/100

def calcular_parcela(valor, taxa, parcelas):
    return valor * ((taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1))

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor



if pode_aprovar(idade_cliente, renda_mensal, emprestimo_desejado):
    taxa_juros = definir_taxa(num_parcelas)
    valor_parcela = calcular_parcela(emprestimo_desejado, taxa_juros, num_parcelas)
    valor_total = calcular_total(valor_parcela, num_parcelas)
    valor_juros = calcular_juros(valor_total, emprestimo_desejado)

    print(f"Cliente: {nome_cliente}")
    print(f"Valor do empréstimo: R${emprestimo_desejado}")
    print(f"Taxa de juros: {taxa_juros * 100}%")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
    print(f"Valor total: R${valor_total:.2f}")
    print(f"Total de juros pagos: R${valor_juros:.2f}")