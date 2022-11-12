import mysql.connector
from mysql.connector import Error 



class Conector():
    def _init_(self) -> Home:
        try:


            Self.conexion= mysql.connector.connect(
            host='localhost',
            port= 3306,
            user='root',
             pasword='contraseña BBDD',
             db='MiBaseDeDatos',
             )

        except mysql.ConnectionError as descripcionErro:
            print("¡No se conecto!")

    def InsertarValor(self, nombre, telefono,direccion):
        if self.conexion.isconnected():
            try:
                cursor=self.conexion.cursor()
                sentenciaSQL="INSERT INTO tabla de ejemplo(%s,%s,%s)"
                datos=(nombre,telefono,direccion)

                cursor.execute(sentenciaSQL,datos)
                self.conexion.commit()
                self.conexion.close()
                
            except:
                 print("No se pudo conectar a la base de datos")

