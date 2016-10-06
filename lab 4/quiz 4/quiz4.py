x = True
frase=0
cagua=0
cfuego=0
agre = []

print("bienvenido")

while x :

        frase = input("digite una frase ")
        if "agua" in frase:
            cagua=cagua+1

        if "fuego" in frase:
            cfuego=cfuego+1
        if "agua" in frase or "fuego" in frase:
            agre.append(frase)
        if frase == "salir":
            x = False
print("cantidad de agua: " ,cagua)
print("cantidad de fuego: " ,cfuego)
print (agre)



