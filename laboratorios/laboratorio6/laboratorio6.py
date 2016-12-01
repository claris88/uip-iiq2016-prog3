print "Escriba la nota de las 5 clases"
nota1 = float(raw_input('Nota1 '))
nota2 = float(raw_input('Nota2 '))
nota3 = float(raw_input('Nota3 '))
nota4 = float(raw_input('Nota4 '))
nota5 = float(raw_input('Nota5 '))
total=nota1+nota2+nota3+nota4+nota5 total=total/5
print "El total de sus 5 calificaciones es: ",total






def Menu():

    print
estudiantes


1) crear estudiante
2) calcular promedio
3) salir
















def menu():

   os.system('clear')

   print"Selecciona una opción"

   print "\t1 - crear estudiante"

   print "\t2 - calcular notas"

    print "\t3 - salir"





while True:

   menu()


   opcionMenu = raw_input("inserta un numero valor >> ")

   if opcionMenu=="1":

      print "introdusca nombre"

      raw_input("Has pulsado la opción 1...\npulsa una tecla para continuar")

   elif opcionMenu=="2":

      print "ingrese notas"

      raw_input("Has pulsado la opción 2...\npulsa una tecla para continuar")

   elif opcionMenu=="3":

      print "salir"

      raw_input("Has pulsado la opción 3...\npulsa una tecla para continuar")

   elif opcionMenu=="9":

      break

   else:

      print ""

      raw_input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

class estudiantes:

    numest = 0
    sumno = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        estudiantes.numest += 1
        estudiantes.sumno += nota

    def mostrarNombreNota(self):
        return(self.nombre, self.nota)

    def mostrarnumest(self):
        return(estudiantes.numest)

    def mostrarsumno(self):
        return(estudiantes.sumno)

    def mostrarNotaMedia(self):
        if estudiantes.numest > 0:
            return(estudiantes.sumno/estudiantes.numest)
        else:
            return("Sin estudiantes")


