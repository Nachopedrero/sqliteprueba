import pandas as pd
import sqlite3 as sq

# Crear una función para ejecutar consultas SQL en la base de datos
def ejecutar_consulta(consulta):
    with sq.connect('tabla.db') as conn:
        cursor = conn.cursor()
        cursor.execute(consulta)
        result = cursor.fetchall()
        return result

# Crear la tabla y cargar los datos
pd.read_csv('Pokemon.csv').to_sql('Pokemon', sq.connect('tabla.db'), if_exists='replace', index=False)

# INSERT un registro
ejecutar_consulta("INSERT INTO Pokemon (Number,Name,Type1,Type2,HP,Attack,Defense,SpAttack,SpDefense,Speed,Total,Image) VALUES (4, 'pepa', 'Poison', 'Psychic', 35, 55, 40, 50, 50, 90, 320, 'null')")

# SELECT un registro
print(ejecutar_consulta("SELECT * FROM Pokemon WHERE Name = 'pepa'"))

# UPDATE un registro
ejecutar_consulta("UPDATE Pokemon SET Name = 'Mewtwo' WHERE Name = 'jacobo'")

# DELETE un registro
ejecutar_consulta("DELETE FROM Pokemon WHERE Name = 'Raichu'")

# SELECT (no se ejecuta porque se eliminó el registro)
print(ejecutar_consulta("SELECT * FROM Pokemon WHERE Name = 'Raichu'"))

# obtener el numero de registros
print(ejecutar_consulta("SELECT COUNT(*) FROM Pokemon"))

# agrupar por tipo
print(ejecutar_consulta("SELECT Type2, COUNT(*) FROM Pokemon GROUP BY Type1"))

# obtener el promedio de ataque
print(ejecutar_consulta("SELECT AVG(Attack) FROM Pokemon"))

# filtrar por ataque mayor que 100
print(ejecutar_consulta("SELECT * FROM Pokemon WHERE Attack > 100"))

# pokemon con defensa entre 20 y 25
print(ejecutar_consulta("SELECT * FROM Pokemon WHERE Defense BETWEEN 20 AND 25"))
