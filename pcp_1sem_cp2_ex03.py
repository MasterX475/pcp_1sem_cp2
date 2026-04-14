# Entrada de dados
cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

#Encontrar a menor nota
menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3
#Calculo das medias
media = (((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + (gs * 0.6))
mediapeso = media * 0.4

print(f"Media do semestre (sem peso) : {media:.1f}")
print(f"Media do semestre com peso: {mediapeso:.1f}")