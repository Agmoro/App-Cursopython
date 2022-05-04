from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Button
from tkinter import ttk
from tkcalendar import DateEntry
import shelve
from tkinter.font import Font
import re

root = Tk()

root.title("Reclamos a Proveedores")
root.configure(background="khaki")
# root.geometry("810x325") quedó anotado por si quiero dejarla de un tamaño fijo
b_font = Font(family="Helvetica", size=11, weight="bold")
b_font2 = Font(family="Helvetica", size=10, weight="bold")

# Definicion de variables #################################################################################

provval, prodval, defval, cantval, fecval, nrecval, mssgval = (
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
)

# label titulo principal ###################################################################################

t_principal = Label(root,
                    text="Registro de Reclamos a Proveedores",
                    bg="khaki",
                    font=b_font2)
t_principal.grid(row=0, columnspan=6, pady=10)

# labels de campos ##########################################################################################

l_proveedor = Label(root, text="Proveedor", bg="khaki")
l_proveedor.grid(row=1, column=0, sticky="w", padx=8)
l_producto = Label(root, text="Producto", bg="khaki")
l_producto.grid(row=2, column=0, sticky="w", padx=8)
l_defecto = Label(root, text="Defecto", bg="khaki")
l_defecto.grid(row=3, column=0, sticky="w", padx=8)
l_cantidad = Label(root, text="Cantidad", bg="khaki")
l_cantidad.grid(row=4, column=0, sticky="w", padx=8)
l_fecha = Label(root, text="Fecha", bg="khaki")
l_fecha.grid(row=5, column=0, sticky="w", padx=8)
l_nreclamo = Label(root, text="N° de Reclamo", bg="khaki")
l_nreclamo.grid(row=8, column=0, sticky="w", padx=8)

fila7 = Label(root, textvariable=mssgval, bg="khaki",
              font=b_font2)  # label de notificaciones
fila7.grid(row=10, column=4, columnspan=2, sticky="n")

# Entries ####################################################################################################

def_cajas = ["dc1", "dc2", "dc3", "dc4"]
def_botellas = ["db1", "db2", "db3", "db4"]
def_etiquetas = ["de1", "de2", "de3", "de4"]
def_tapas = ["dt1", "dt2", "dt3", "dt4"]
def_film = ["df1", "df2", "df3", "df4"]
prod_cajas = ["pc1", "pc2", "pc3", "pc4"]
prod_etiquetas = ["pe1", "pe2", "pe3", "pe4"]
prod_tapas = ["pt1", "pt2", "pt3", "pt4"]
prod_botellas = ["pb1", "pb2", "pb3", "pb4"]
prod_film = ["pf1", "pf2", "pf3", "pf4"]


class Proveedor():
    mis_proveedores = []

    def __init__(self, nombre, productos, defectos):
        self.nombre = nombre
        self.defectos = defectos
        self.productos = productos
        self.__class__.mis_proveedores.append(self)


cartocor = Proveedor("Cartocor", prod_cajas, def_cajas)
cattorini = Proveedor("Cattorini Hnos.", prod_botellas, def_botellas)
multilabel = Proveedor("Multilabel", prod_etiquetas, def_etiquetas)
guala = Proveedor("Guala", prod_tapas, def_tapas)
islagrande = Proveedor("Isla Grande", prod_film, def_film)

nom_prov = []
runs = 0


def genlist(nom_prov):
    for x in range(0, len(Proveedor.mis_proveedores), 1):
        nom_prov.append(Proveedor.mis_proveedores[x].nombre)


if runs == 0:
    genlist(nom_prov)
    runs += 1

# e_proveedor = Entry(root, textvariable=provval, bg="white")
e_proveedor = ttk.Combobox(root, values=nom_prov, width=18, state="normal")
e_proveedor.grid(row=1, column=1, padx=10, pady=3)
e_proveedor.current(0)
# e_producto = Entry(root, textvariable=prodval, bg="white")
e_producto = ttk.Combobox(root, values=prod_cajas, width=18, state="normal")
e_producto.grid(row=2, column=1, padx=10, pady=3)
e_producto.current(0)
# e_defecto = Entry(root, textvariable=defval, bg="white")
e_defecto = ttk.Combobox(root, values=def_cajas, width=18, state="normal")
e_defecto.grid(row=3, column=1, padx=10, pady=3)
e_defecto.current(0)
e_cantidad = Entry(root, textvariable=cantval, bg="white", width=19)
e_cantidad.grid(row=4, column=1, padx=10, pady=3)
e_fecha = DateEntry(root, selectmode="day", bg="white", width=18, date_pattern='dd/MM/yyyy')
e_fecha.grid(row=5, column=1, padx=10, pady=3)
e_nreclamo = Entry(root, textvariable=nrecval, bg="white")
e_nreclamo.grid(row=8, column=1, padx=10, pady=3)

# Funciones ##########################


def setlists(event):
    for x in range(0, len(Proveedor.mis_proveedores), 1):
        if Proveedor.mis_proveedores[x].nombre == e_proveedor.get():
            e_producto['values'] = Proveedor.mis_proveedores[x].productos
            e_defecto['values'] = Proveedor.mis_proveedores[x].defectos
            e_producto.current(0)
            e_defecto.current(0)


e_proveedor.bind('<<ComboboxSelected>>', setlists)


def Listar():
    mssgval.set("")
    mssgval.set("Listando últimos 10 reclamos")
    db = shelve.open("reclamos")
    arbol.delete(
        *arbol.get_children()
    )  # lo que entiendo del splat * aca es que hace unpack de un item sin saber cuantos valores tiene, si lo saco no funciona
    filas = db.get("nreclamo")

    if filas == None:
        mssgval.set("Faltan cargar datos")
    else:
        contar = 0
        for i in list(range(filas, filas - 10, -1)):
            try:
                arbol.insert(
                    parent="",
                    index="end",
                    iid=contar,
                    text="",
                    values=list(db[str(i)].values()),
                )
                contar += 1
            except:
                continue
    db.close


def Guardar(proveedor, producto, defecto, cantidad, fecha):
    mssgval.set("")
    if (proveedor == "" or producto == "" or defecto == "" or cantidad == ""
            or fecha == ""):
        mssgval.set("Completa todos los campos arriba de Guardar")
    else:
        db = shelve.open("reclamos")
        nreclamo = db.get("nreclamo")
        if nreclamo == None:
            nreclamo = 1
        else:
            nreclamo += 1
        db["nreclamo"] = nreclamo
        reclamo = {}
        reclamo["reclamo n°"] = nreclamo
        reclamo["fecha"] = fecha
        reclamo["proveedor"] = proveedor
        reclamo["producto"] = producto
        reclamo["defecto"] = defecto
        reclamo["cantidad"] = cantidad
        db[str(nreclamo)] = reclamo
        e_proveedor.current(0)
        e_producto.delete(0, "end")
        e_producto["values"] = ""
        e_defecto.delete(0, "end")
        e_defecto["values"] = ""
        e_cantidad.delete(0, "end")
        e_fecha.delete(0, "end")

        mssgval.set("Se generó el reclamo N°: " + str(nreclamo))
        arbol.delete(*arbol.get_children())
        arbol.insert(
            parent="",
            index="end",
            iid=0,
            text="",
            values=list(db[str(nreclamo)].values()),
        )
        db.close


def Mostrar(numreclamo):
    mssgval.set("")
    arbol.delete(*arbol.get_children())
    try:
        if not re.match("^[0-9]+$", nrecval.get()):
            mssgval.set("N° de reclamo necesita números")
            e_nreclamo.delete(0, "end")
        else:
            db = shelve.open("reclamos")
            try:
                arbol.insert(
                    parent="",
                    index="end",
                    iid=0,
                    text="",
                    values=list(db[str(numreclamo)].values()),
                )
            except:
                mssgval.set("N° de reclamo no encontrado")

            finally:
                e_nreclamo.delete(0, "end")

            db.close
    except:
        mssgval.set("N° de reclamo no existe")
        e_nreclamo.delete(0, "end")


def Modificar(proveedor, producto, defecto, cantidad, fecha, numreclamo):
    mssgval.set("")
    db = shelve.open("reclamos")
    try:
        if not re.match("^[0-9]+$", nrecval.get()):
            mssgval.set("Ingresa números en N° de reclamo")
            e_nreclamo.delete(0, "end")
        elif (proveedor == "" and producto == "" and defecto == ""
              and cantidad == "" and fecha == ""):
            mssgval.set("Completa al menos 1 campo arriba de Guardar")
        elif db[numreclamo].get("reclamo n°") == None:
            mssgval.set("N° de reclamo no existente")
        else:
            reclamo = {}
            reclamo["reclamo n°"] = numreclamo
            if fecha != "":
                reclamo["fecha"] = fecha
            else:
                reclamo["fecha"] = db[numreclamo]["fecha"]
            if proveedor != "":
                reclamo["proveedor"] = proveedor
            else:
                reclamo["proveedor"] = db[numreclamo]["proveedor"]
            if producto != "":
                reclamo["producto"] = producto
            else:
                reclamo["producto"] = db[numreclamo]["producto"]
            if defecto != "":
                reclamo["defecto"] = defecto
            else:
                reclamo["defecto"] = db[numreclamo]["defecto"]
            if cantidad != "":
                reclamo["cantidad"] = cantidad
            else:
                reclamo["cantidad"] = db[numreclamo]["cantidad"]

            db[numreclamo] = reclamo
            e_nreclamo.delete(0, "end")
            e_proveedor.delete(0, "end")
            e_producto.delete(0, "end")
            e_defecto.delete(0, "end")
            e_cantidad.delete(0, "end")
            e_fecha.delete(0, "end")
            mssgval.set("Se modificó el reclamo N°: " + str(numreclamo))
            arbol.delete(*arbol.get_children())
            arbol.insert(
                parent="",
                index="end",
                iid=0,
                text="",
                values=list(db[str(numreclamo)].values()),
            )
            db.close
    except:
        mssgval.set("N° de reclamo no hayado")
        e_nreclamo.delete(0, "end")
        e_proveedor.delete(0, "end")
        e_producto.delete(0, "end")
        e_defecto.delete(0, "end")
        e_cantidad.delete(0, "end")
        e_fecha.delete(0, "end")


def Borrar(numreclamo):
    try:
        if numreclamo == "":
            mssgval.set("Todo limpio, ingrese N° de reclamo a borrar")
            e_nreclamo.delete(0, "end")
            e_proveedor.delete(0, "end")
            e_producto.delete(0, "end")
            e_defecto.delete(0, "end")
            e_cantidad.delete(0, "end")
            e_fecha.delete(0, "end")
            arbol.delete(*arbol.get_children())
        elif not re.match("^[0-9]+$", nrecval.get()):
            mssgval.set("Falta algun número en N° de reclamo")
            e_nreclamo.delete(0, "end")
        else:
            db = shelve.open("reclamos")
            del db[numreclamo]
            mssgval.set("Se ha borrado el reclamo N° " + numreclamo)
            e_nreclamo.delete(0, "end")

    except:
        mssgval.set("N° de reclamo no hayado")
        e_nreclamo.delete(0, "end")


# Botones ##################################################################################################

b_guardar = Button(
    root,
    text="Guardar",
    borderwidth=4,
    command=lambda: Guardar(e_proveedor.get(), e_producto.get(), e_defecto.get(
    ), cantval.get(), fecval.get()),
    fg="black",
    bg="gold2",
    width=13,
    font=b_font,
)
b_guardar.grid(row=6, column=1, pady=5)

b_mostrar = Button(
    root,
    text="Mostrar",
    borderwidth=4,
    command=lambda: Mostrar(nrecval.get()),
    fg="black",
    bg="gold2",
    width=13,
    font=b_font,
)
b_mostrar.grid(row=9, column=1, pady=5)

b_modificar = Button(
    root,
    text="Modificar",
    borderwidth=4,
    command=lambda: Modificar(
        provval.get(),
        prodval.get(),
        defval.get(),
        cantval.get(),
        fecval.get(),
        nrecval.get(),
    ),
    fg="black",
    bg="gold2",
    width=13,
    font=b_font,
)
b_modificar.grid(row=10, column=1, pady=5)

b_borrar = Button(
    root,
    text="Borrar",
    borderwidth=4,
    command=lambda: Borrar(nrecval.get()),
    fg="black",
    bg="gold2",
    width=10,
    font=b_font,
)
b_borrar.grid(row=10, column=0, pady=5, padx=5)

b_listar = Button(
    root,
    text="Listar",
    borderwidth=4,
    command=lambda: Listar(),
    fg="black",
    bg="gold2",
    width=10,
    font=b_font,
)
b_listar.grid(row=9, column=0, pady=3, padx=5)

# Treeview ##################################################################################################

arbol = ttk.Treeview(root)
arbol["columns"] = ("N°", "Fecha", "Proveedor", "Producto", "Defecto",
                    "Cantidad")

arbol.column("#0", width=0, stretch="no")
arbol.column("N°", anchor="center", width=40)
arbol.column("Fecha", anchor="w", width=60)
arbol.column("Proveedor", anchor="w", width=120)
arbol.column("Producto", anchor="w", width=120)
arbol.column("Defecto", anchor="w", width=120)
arbol.column("Cantidad", anchor="center", width=80)

arbol.heading("#0", text="")
arbol.heading("N°", text="N°", anchor="center")
arbol.heading("Fecha", text="Fecha", anchor="center")
arbol.heading("Proveedor", text="Proveedor", anchor="w")
arbol.heading("Producto", text="Producto", anchor="w")
arbol.heading("Defecto", text="Defecto", anchor="w")
arbol.heading("Cantidad", text="Cantidad", anchor="center")

arbol.grid(row=1, rowspan=9, column=4, padx=5, pady=4, sticky="n")

root.mainloop()
