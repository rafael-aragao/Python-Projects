#Boletim Escolar - Matéria Matemática

nota1 = 10
nota2 = 10
nota3 = 10
nota4 = 10

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média de matemática foi: {media}")

#Para ser aprovado sua nota deve ser maior que 7

if media >= 10:
    print("Maravilindo")
elif media >= 9:
    print("Espetaculoso")
elif media >=7:
    print("Aprovado")
else:
    print("Reprovado")