import unittest

#Programa que al insertar ej: Franco, Zapata, dict.
#Tiene que detectar si ese nombre y apellido le pertenece a alguna persona del diccionario.

def buscar_datos(*args,**kwargs):
    
    #Falta que funcione insertando los datos desordenados.

    for clave, personas in kwargs.items():
        
        if list(args) == list(personas.values()):

            return clave
    
    return False


database = {
    "persona1": {
            "primer_nombre": "Pablo",
            "segundo_nombre": "Diego",
            "primer_apellido": "Ruiz",
            "segundo_apellido": "Picasso"
    },
    "persona2": {
            "primer_nombre": "Franco",
            "segundo_nombre": "Agustin",
            "primer_apellido": "Zapata",
            "segundo_apellido": ""
    }
}

buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)

class TestBuscarDatos(unittest.TestCase):
    
    def test_1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,"persona1")

    def test_2(self):
        resultado = buscar_datos("Franco", "Agustin", "Zapata", "", **database)
        self.assertEqual(resultado,"persona2")

    def test_False(self):
        resultado = buscar_datos("Juan", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,False)


unittest.main()