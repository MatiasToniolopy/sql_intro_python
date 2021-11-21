#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

from abc import abstractmethod
import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    conexion = sqlite3.connect('secundaria.db')
    cursor = conexion.cursor()
    
    datos = [('matias toniolo', 36, 1, 'inove'),
             ('sergio perez', 44, 2, 'susana gimenez'),
             ('natalia luna', 33, 3, 'sandro loria'),
             ('miriam gonzalez', 39, 4, 'mirtha legrand'),
             ('nahuel anderson', 21, 5, 'carlos bianchi'),
             ('lorena pomina', 52, 6, 'carlos bilardo')]
    cursor.executemany("INSERT INTO estudiante VALUES(NULL,?,?,?,?)", datos)
    conexion.commit()
    conexion.close()
    
    


def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    conexion = sqlite3.connect('secundaria.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante")
    while True:
        r = cursor.fetchone()
        if r is None:
            break
        print(r)
    
    conexion.close()
    
    
    


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conexion = sqlite3.connect('secundaria.db')
    cursor = conexion.cursor()
    for row in cursor.execute('SELECT id, name, age FROM estudiante WHERE grade =?', (grade,)):
        print(row)
    
    conexion.close()
    
    


def insert():
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conexion = sqlite3.connect('secundaria.db')
    cursor = conexion.cursor()
    ingresos = [('eleonora casano', 77, 3, 'crintino ronaldo'),
                ('ricardo fort', 51, 1, 'fel fort'),
                ('eduardo martiniano', 39, 5, 'alejandro fantino')]
    cursor.executemany("INSERT INTO estudiante VALUES(NULL,?,?,?,?)", ingresos)
    conexion.commit()
    conexion.close()


def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    conexion = sqlite3.connect('secundaria.db')
    cursor = conexion.cursor()
    b = cursor.execute("UPDATE estudiante SET name=? WHERE id=?", (name, id))
    conexion.commit()
    conexion.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    fetch()

    grade = 3
    search_by_grade(grade)

    insert()

    name = '¿Inove?'
    id = 2
    modify(id, name)
