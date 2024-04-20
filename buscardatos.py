import unittest

def buscar_datos(*args,**kwargs):
    

    for clave, personas in kwargs.items():
        
        lista_argumentos = list(args)
        lista_atributos = list(personas.values())

        for elemento in lista_atributos:
            
            if elemento == "":
                lista_atributos.remove(elemento)
            else:
                pass


        if lista_argumentos == lista_atributos:

            return clave

        i=0        
        for arg in lista_argumentos:

            if arg == "":
                lista_argumentos.remove("")

            
            if arg in lista_atributos:
                i = i + 1

        
        if i == len(lista_atributos):
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

class TestBuscarDatos(unittest.TestCase):
    
    def test_1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,"persona1")

    def test_1b(self):
        resultado = buscar_datos("Diego", "Pablo", "Picasso", "Ruiz", **database)
        self.assertEqual(resultado,"persona1")

    def test_2(self):
        resultado = buscar_datos("Franco", "Agustin", "Zapata", "", **database)
        self.assertEqual(resultado,"persona2")

    def test_2b(self):
        resultado = buscar_datos("Zapata", "Franco","Agustin", "", **database)
        self.assertEqual(resultado,"persona2")

    def test_2c(self):
        resultado = buscar_datos("Zapata", "Franco","Agustin", **database)
        self.assertEqual(resultado,"persona2")

    def test_False(self):
        resultado = buscar_datos("Juan", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,False)

    def test_error(self):
        resultado = buscar_datos("123", "111","222", **database)
        self.assertEqual(resultado,False)


unittest.main()