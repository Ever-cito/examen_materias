import psycopg2
class Conexion:

    """Metodo contructor de la materia
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenbd user=postgres host=localhost password=13579")
        
        """getConexion

            retorna la instancia de la base de datos
        """
    def getConexion(self):
        return self.con 