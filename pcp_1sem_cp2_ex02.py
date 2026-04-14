#Lados do Triângulo

lado_a = float(input("Lado A = "))
lado_b = float(input("Lado B = "))
lado_c = float(input("Lado C = "))

if lado_a < lado_b:
    lado_x = lado_b
    lado_b = lado_a
    lado_a = lado_x

if lado_a < lado_c:
    lado_x = lado_c
    lado_c = lado_a
    lado_a = lado_x

if lado_a >= lado_b + lado_c:
    print(f"Não forma triângulo")
    quit()
elif lado_a**2 == lado_b**2 + lado_c**2:
    print(f"Triângulo Retângulo")
elif lado_a**2 > lado_b**2 + lado_c**2:
    print(f"Triângulo Obtusângulo")
elif lado_a**2 < lado_b**2 + lado_c**2:
    print(f"Triângulo Acutângulo")
if lado_a == lado_b == lado_c:
    print(f"Triângulo Equilatero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(f"Triângulo Isosceles")