import sqlite3
import re


id_item_seleccionado = ""
variable_regex = 0


def conexion():
    con = sqlite3.connect("adoptame.db")
    return con


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE candidatos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre varchar(40) NOT NULL,
             telefono int NOT NULL,
             casa varchar(40),
             mascotas varchar(80),
             sexo varchar(20),
             tamano varchar(20),
             edad varchar(20))
    """
    cursor.execute(sql)
    con.commit()


try:
    conexion()
    crear_tabla()
except:
    print("La base de datos ya ha sido creada")


def guardar(nombre, telefono, casa, otras, sexo, tamaño, edad, tree):
    cadena = telefono
    patron = "\d{10}"
    global variable_regex
    if re.match(patron, cadena):  # que use el patron para verificar la cadena
        variable_regex = 1
        con = conexion()
        cursor = con.cursor()
        data = (nombre, telefono, casa, otras, sexo, tamaño, edad)
        sql = "INSERT INTO candidatos(nombre,telefono,casa,mascotas,sexo,tamano,edad) VALUES(?,?,?,?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()
        actualizar_treeview(tree)
    else:
        variable_regex = 0

    return variable_regex


def borrar(tree):
    valor = tree.selection()  # trae un valor raro, de la fila seleccionada
    item = tree.item(
        valor
    )  # trae todos los elementos de la fila en un diccionario (yo quiero el id)
    mi_id = item["text"]
    con = conexion()
    cursor = con.cursor()
    data = (mi_id,)  # hace tupla
    sql = "DELETE FROM candidatos WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()  # hasta aca me borra de la base de datos
    tree.delete(valor)  # me borra de la vista


def modificar(nombre, telefono, casa, otras, sexo, tamano, edad, tree):
    valor = tree.selection()  # trae un valor raro, de la fila seleccionada
    item = tree.item(
        valor
    )  # trae todos los elementos de la fila en un diccionario (yo quiero el id)
    mi_id = item["text"]
    con = conexion()
    cursor = con.cursor()
    data = (nombre, telefono, casa, otras, sexo, tamano, edad, mi_id)
    sql = "UPDATE candidatos SET nombre=?, telefono=?, casa=?, mascotas=?, sexo=?, tamano=?,edad=? WHERE ID=?"  # instruccion de sql
    cursor.execute(
        sql, data
    )  # le estoy pdiiendo a la base de datos que lo ejecute y una vez que lo haga:
    con.commit()  # hacelo
    actualizar_treeview(tree)


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM candidatos ORDER BY id ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        mitreview.insert(
            "",
            0,
            text=fila[0],
            values=(
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
            ),
        )
