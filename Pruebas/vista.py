from tkinter import Tk
from tkinter import StringVar
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import ttk

import modelo


def vista_principal(root):

    root.title("ADOPTAME")
    root.geometry("720x640")
    # root.iconbitmap("icono.ico")
    ######## variables#######

    var_1 = StringVar()
    var_2 = StringVar()
    var_3 = StringVar()
    var_4 = StringVar()
    var_5 = StringVar()
    var_6 = StringVar()
    var_7 = StringVar()
    w_ancho = 30
    texto_consola = StringVar()
    id_item_selecionado = modelo.id_item_seleccionado

    # ------------------------

    marco = Frame()
    marco.pack(fill="both", expand="yes")

    titulo = Label(marco, text="¡Adoptame!")
    titulo.config(bg="#9E63BA", font=("Verdana", 24), fg="white")
    titulo.pack(fill="x")

    marco_cuerpo = Frame(marco)
    marco_cuerpo.pack(side="top", fill="both", expand="yes")

    # -----------DATOS------------

    marco_datos = Frame(marco_cuerpo)
    marco_datos.config(bg="#93BDDB")
    marco_datos.pack(side="left", anchor="w", fill="both", expand="yes", pady=5, padx=5)

    titulo_datos = Label(marco_datos, text="Datos personales")
    titulo_datos.config(bg="#7EA3BD", font=("Verdana", 16), fg="white")
    titulo_datos.pack(fill="x")

    titulo_nombre = Label(marco_datos, text="Nombre y Apellido")
    titulo_nombre.config(bg="#93BDDB", font=("Verdana", 10, "bold"))
    titulo_nombre.pack(anchor="w", side="top", padx=10)
    titulo_nombre2 = Label(marco_datos, text="Hasta 40 caracteres")
    titulo_nombre2.config(bg="#93BDDB", font=("Verdana", 8))
    titulo_nombre2.pack(anchor="w", side="top", padx=10)
    nombre = Entry(marco_datos, textvariable=var_1, width=w_ancho, state="disable")
    nombre.pack(anchor="w", side="top", padx=10)

    titulo_telefono = Label(marco_datos, text="Teléfono")
    titulo_telefono.config(bg="#93BDDB", font=("Verdana", 10, "bold"))
    titulo_telefono.pack(anchor="w", side="top", padx=10)
    titulo_telefono2 = Label(marco_datos, text="10 dígitos")
    titulo_telefono2.config(bg="#93BDDB", font=("Verdana", 8))
    titulo_telefono2.pack(anchor="w", side="top", padx=10)
    telefono = Entry(marco_datos, textvariable=var_2, width=w_ancho, state="disable")
    telefono.pack(anchor="w", side="top", padx=10)

    titulo_casa = Label(marco_datos, text="Tipo de casa")
    titulo_casa.config(bg="#93BDDB", font=("Verdana", 10, "bold"))
    titulo_casa.pack(anchor="w", side="top", padx=10)
    titulo_casa = Label(marco_datos, text="Ej: Casa con patio, departamento")
    titulo_casa.config(bg="#93BDDB", font=("Verdana", 8))
    titulo_casa.pack(anchor="w", side="top", padx=10)
    casa = Entry(marco_datos, textvariable=var_3, width=w_ancho, state="disable")
    casa.pack(anchor="w", side="top", padx=10)

    titulo_otras = Label(marco_datos, text="Otras mascotas")
    titulo_otras.config(bg="#93BDDB", font=("Verdana", 10, "bold"))
    titulo_otras.pack(anchor="w", side="top", padx=10)
    titulo_otras = Label(marco_datos, text="V-ᴥ-V ᵒᴥᵒ (ᵔᴥᵔ)")
    titulo_otras.config(bg="#93BDDB", font=("Verdana", 8))
    titulo_otras.pack(anchor="w", side="top", padx=10)
    otras = Entry(marco_datos, textvariable=var_4, width=w_ancho, state="disable")
    otras.pack(anchor="w", side="top", padx=10)

    # -------------------REQUISITOS---------------
    marco_requisitos = Frame(marco_cuerpo)
    marco_requisitos.config(bg="#EDCA82")
    marco_requisitos.pack(side="left", fill="both", expand="yes", pady=5, padx=5)

    titulo_requisitos = Label(marco_requisitos, text="Requisitos")
    titulo_requisitos.config(bg="#D4B474", font=("Verdana", 16), fg="white")
    titulo_requisitos.pack(fill="x")

    titulo_sexo = Label(marco_requisitos, text="Sexo")
    titulo_sexo.config(bg="#EDCA82", font=("Verdana", 10, "bold"))
    titulo_sexo.pack(anchor="w", side="top", padx=10)
    titulo_sexo = Label(marco_requisitos, text="Macho/Hembra")
    titulo_sexo.config(bg="#EDCA82", font=("Verdana", 8))
    titulo_sexo.pack(anchor="w", side="top", padx=10)
    sexo = Entry(marco_requisitos, textvariable=var_5, width=w_ancho, state="disable")
    sexo.pack(anchor="w", side="top", padx=10)

    titulo_tamano = Label(marco_requisitos, text="Tamaño")
    titulo_tamano.config(bg="#EDCA82", font=("Verdana", 10, "bold"))
    titulo_tamano.pack(anchor="w", side="top", padx=10)
    titulo_tamano = Label(marco_requisitos, text="Chico/Mediano/Grande")
    titulo_tamano.config(bg="#EDCA82", font=("Verdana", 8))
    titulo_tamano.pack(anchor="w", side="top", padx=10)
    tamano = Entry(marco_requisitos, textvariable=var_6, width=w_ancho, state="disable")
    tamano.pack(anchor="w", side="top", padx=10)

    titulo_edad = Label(marco_requisitos, text="Edad")
    titulo_edad.config(bg="#EDCA82", font=("Verdana", 10, "bold"))
    titulo_edad.pack(anchor="w", side="top", padx=10)
    titulo_edad = Label(marco_requisitos, text="Cachorro/Adulto/Mayor")
    titulo_edad.config(bg="#EDCA82", font=("Verdana", 8))
    titulo_edad.pack(anchor="w", side="top", padx=10)
    edad = Entry(marco_requisitos, textvariable=var_7, width=w_ancho, state="disable")
    edad.pack(anchor="w", side="top", padx=10)

    # -------------------TREEVIEW----------------

    marco_grilla = Frame(marco)
    marco_grilla.pack(side="top", anchor="n", fill="both", expand="yes", pady=5, padx=5)

    tree = ttk.Treeview(marco_grilla)
    tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
    tree.column("#0", width=40, anchor="w")
    tree.column("col1", width=130)
    tree.column("col2", width=90)
    tree.column("col3", width=110)
    tree.column("col4", width=110)
    tree.column("col5", width=70)
    tree.column("col6", width=70)
    tree.column("col7", width=90)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Nombre")
    tree.heading("col2", text="Teléfono")
    tree.heading("col3", text="Tipo de casa")
    tree.heading("col4", text="Otras mascotas")
    tree.heading("col5", text="Sexo")
    tree.heading("col6", text="Tamaño")
    tree.heading("col7", text="Edad")
    tree.pack()

    # -------------------BOTONES---------------

    marco_botones = Frame(marco_cuerpo)
    marco_botones.pack(side="right", anchor="e", fill="both", expand="yes", pady="55")

    def estado_boton(estado1, estado2, estado3, estado4, estado5, estado6):
        boton_nuevo.configure(state=estado1)
        boton_guardar.configure(state=estado2)
        boton_borrar.configure(state=estado3)
        boton_ver.configure(state=estado4)
        boton_modificar.configure(state=estado5)
        boton_cancelar.configure(state=estado6)

    def estado_campos(estado1, estado2, estado3, estado4, estado5, estado6, estado7):
        nombre.configure(state=estado1)
        telefono.configure(state=estado2)
        casa.configure(state=estado3)
        otras.configure(state=estado4)
        sexo.configure(state=estado5)
        tamano.configure(state=estado6)
        edad.configure(state=estado7)

    def nuevo_vista(tree):
        tree.selection_clear()
        estado_campos(
            "normal", "normal", "normal", "normal", "normal", "normal", "normal"
        )
        estado_boton("disable", "normal", "disable", "disable", "disable", "normal")

    boton_nuevo = Button(marco_botones, text="Nuevo", command=lambda: nuevo_vista(tree))
    boton_nuevo.config(width="8", height="1")
    boton_nuevo.pack(pady="3")

    def borrar_campos_vista():
        var_1.set("")
        var_2.set("")
        var_3.set("")
        var_4.set("")
        var_5.set("")
        var_6.set("")
        var_7.set("")

    def guardar_vista():

        variable_guardar = modelo.guardar(
            var_1.get(),
            var_2.get(),
            var_3.get(),
            var_4.get(),
            var_5.get(),
            var_6.get(),
            var_7.get(),
            tree,
        )
        if modelo.variable_regex == 1:
            texto_consola.set("Registro actualizado exitosamente")
            borrar_campos_vista()
            estado_campos(
                "disable",
                "disable",
                "disable",
                "disable",
                "disable",
                "disable",
                "disable",
            )
            estado_boton("normal", "disable", "disable", "normal", "disable", "disable")
        elif modelo.variable_regex == 0:
            texto_consola.set("El número de teléfono debe tener 10 dígitos")

    boton_guardar = Button(marco_botones, text="Guardar", command=guardar_vista)
    boton_guardar.config(width="8", height="1")
    boton_guardar.pack(pady="3")

    def borrar_vista():
        variable_borrar = modelo.borrar(tree)
        texto_consola.set("Registro eliminado exitosamente")
        borrar_campos_vista()
        estado_campos(
            "disable", "disable", "disable", "disable", "disable", "disable", "disable"
        )
        estado_boton("normal", "disable", "disable", "normal", "disable", "disable")

    boton_borrar = Button(marco_botones, text="Eliminar", command=borrar_vista)
    boton_borrar.config(width="8", height="1")
    boton_borrar.pack(pady="3")

    def ver_vista(tree):
        record = tree.selection()
        item = tree.item(record)
        valor = item["values"]
        var_1.set(valor[0])
        var_2.set(valor[1])
        var_3.set(valor[2])
        var_4.set(valor[3])
        var_5.set(valor[4])
        var_6.set(valor[5])
        var_7.set(valor[6])
        estado_campos(
            "normal", "normal", "normal", "normal", "normal", "normal", "normal"
        )
        estado_boton("disable", "disable", "normal", "disable", "normal", "normal")

    boton_ver = Button(marco_botones, text="Ver", command=lambda: ver_vista(tree))
    boton_ver.config(width="8", height="1")
    boton_ver.pack(pady="3")

    def modificar_vista():
        variable_modificarr = modelo.modificar(
            var_1.get(),
            var_2.get(),
            var_3.get(),
            var_4.get(),
            var_5.get(),
            var_6.get(),
            var_7.get(),
            tree,
        )
        borrar_campos_vista()
        estado_campos(
            "disable", "disable", "disable", "disable", "disable", "disable", "disable"
        )
        estado_boton("normal", "disable", "disable", "normal", "disable", "disable")
        texto_consola.set("Registro modificado exitosamente")

    boton_modificar = Button(marco_botones, text="Modificar", command=modificar_vista)
    boton_modificar.config(width="8", height="1")
    boton_modificar.pack(pady="3")

    def cancelar_vista():
        borrar_campos_vista()
        estado_campos(
            "disabled",
            "disabled",
            "disabled",
            "disabled",
            "disabled",
            "disabled",
            "disabled",
        )
        estado_boton("normal", "disable", "disable", "normal", "disable", "disable")

    boton_cancelar = Button(marco_botones, text="Cancelar", command=cancelar_vista)
    boton_cancelar.config(width="8", height="1")
    boton_cancelar.pack(pady="3")

    marco_consola = Frame(marco)
    marco_consola.config(bg="black")
    marco_consola.pack(fill="both", expand="yes")

    label_consola = Label(marco_consola, textvariable=texto_consola, font=("Arial", 20))
    label_consola.config(bg="black", fg="white")
    label_consola.pack()

    estado_boton("normal", "disable", "disable", "normal", "disable", "disable")
    modelo.actualizar_treeview(tree)

    texto_consola.set("Bienvenido")
