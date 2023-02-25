import unittest
def agregar_nueva_bebida(bebida):
    if len(bebida) == 0:
        return "Sin bebida"

    # Eliminar los espacios en blanco en la entrada
    beb_limp = bebida.replace(" ", "")
    
    # Separar el nombre de la bebida y los tamaños usando la coma como separador
    elementos = beb_limp.split(",")
    
    # Validar que se ingresó al menos un tamaño
    if len(elementos) < 2:
        return "No se insertó un tamaño"
    
    # Validar que no se ingresaron más de cinco tamaños
    if len(elementos) > 6:
        return "Demasiados tamaños"
    
    # Validar el nombre de la bebida
    nombre_bebida = elementos[0]
    if not nombre_bebida.isalpha() or len(nombre_bebida) < 2 or len(nombre_bebida) > 15 :
        return "Nombre no es válido"
    
    # Validar los tamaños
    tamanos = elementos[1:]
    tamanos_validos = []
    for t in tamanos:
        try:
            # Convertir el tamaño a entero y validar que esté dentro del rango
            tam = int(t)
            if tam < 1 or tam > 48:
                return "Tamaño fuera del rango"
            # Validar que los tamaños estén en orden ascendente
            if tamanos_validos and tam <= tamanos_validos[-1]:
                return "Orden de los tamaños es incorrecto"
            tamanos_validos.append(tam)
        except ValueError:
            # Si no se puede convertir el tamaño a entero, es inválido
            return "Tamaño no es entero"

    #Prueba con impresion      
    #bebida_imp = nombre_bebida + "," + ",".join(str(t) for t in tamanos_validos)
    
    return "Bebida registrada con exito"


class Testagregar_nueva_bebida(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(agregar_nueva_bebida("Horchata, 3, 5, 7"), "Bebida registrada con exito")
        self.assertEqual(agregar_nueva_bebida("Pepsi, 5, 6, 42"), "Bebida registrada con exito")
        self.assertEqual(agregar_nueva_bebida("Jamaica, 1, 2, 3"), "Bebida registrada con exito")

    def test_nomNoAlfabetico(self):
        self.assertEqual(agregar_nueva_bebida("Coca_cola, 2, 6, 12"), "Nombre no es válido")
        self.assertEqual(agregar_nueva_bebida("Pepsi light., 8, 10, 12"), "Nombre no es válido")
      
    def test_nomLongMenor(self):
        self.assertEqual(agregar_nueva_bebida("C, 3, 45, 46"), "Nombre no es válido")
        self.assertEqual(agregar_nueva_bebida(", 2, 4"), "Nombre no es válido")
      
    def test_nomLongMayor(self):
        self.assertEqual(agregar_nueva_bebida("Coca cola Light zero, 5, 8, 12"), "Nombre no es válido")
        self.assertEqual(agregar_nueva_bebida("Agua de Horchata con toque de canela, 2, 4, 12"), "Nombre no es válido")
    
    def test_tamMenor(self):
        self.assertEqual(agregar_nueva_bebida("Coca cola, 0, 2, 12"), "Tamaño fuera del rango")
        self.assertEqual(agregar_nueva_bebida("Jamaica, -19, 4, 12"), "Tamaño fuera del rango")
      
    def test_tamMayor(self):
        self.assertEqual(agregar_nueva_bebida("Pepsi, 1, 4, 14, 49"), "Tamaño fuera del rango")
        self.assertEqual(agregar_nueva_bebida("Horchata, 19, 20, 200"), "Tamaño fuera del rango")
      
    def test_tamDecimal(self):
        self.assertEqual(agregar_nueva_bebida("Fanta, 1.1, 4, 14"), "Tamaño no es entero")
        self.assertEqual(agregar_nueva_bebida("Rompope, 19, 20, 20.5"), "Tamaño no es entero")
      
    def test_tamNoNumerico(self):
        self.assertEqual(agregar_nueva_bebida("Jamaica, chica, mediana, grande"), "Tamaño no es entero")
        self.assertEqual(agregar_nueva_bebida("Horchata, 5, mediana, 10"), "Tamaño no es entero")
   
    def test_tamCantMenor(self):
        self.assertEqual(agregar_nueva_bebida("Manzanita"), "No se insertó un tamaño")
        self.assertEqual(agregar_nueva_bebida("Squirt"), "No se insertó un tamaño")
      
    def test_tamCantMayor(self):
        self.assertEqual(agregar_nueva_bebida("Pepsi, 1, 2, 3, 4, 5, 6"),"Demasiados tamaños")
        self.assertEqual(agregar_nueva_bebida("Fanta, 2, 4, 6, 8, 10, 12, 14, 16"), "Demasiados tamaños")
    def test_Desorden(self):
        self.assertEqual(agregar_nueva_bebida("Manzanita, 1,4,3,2"), "Orden de los tamaños es incorrecto")
        self.assertEqual(agregar_nueva_bebida("Squirt, 10, 9, 1"), "Orden de los tamaños es incorrecto")
    def test_tamVacio(self):
        self.assertEqual(agregar_nueva_bebida("Margarita, ,4,5,6"), "Tamaño no es entero")
        self.assertEqual(agregar_nueva_bebida("Squirt, 10, ,11"), "Tamaño no es entero")
    def test_nomVacio(self):
        self.assertEqual(agregar_nueva_bebida(""), "Sin bebida")
        self.assertEqual(agregar_nueva_bebida(""), "Sin bebida")
      
if __name__ == '__main__':
    unittest.main()