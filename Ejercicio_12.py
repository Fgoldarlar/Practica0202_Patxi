letra = input("Dime una letra")
frase = input("Dime una frase")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(letra, contador, frase)