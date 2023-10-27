Nombre = input("Buenas, digame su nombre")
genero = input("A continuación, digame si es hombre (H) o Mujer (M)")
if genero == "H":
    if Nombre.lower() < "m":
        casa = "Slytherin"
    else:
        casa = "Gryffindor"
else:
    if Nombre.lower() > "n":
        casa = "Slytherin"
    else:
        casa = "Gryffindor"
print("Tu casa es", casa)






    
