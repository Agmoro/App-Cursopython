import shelve
from tkinter import messagebox
import re

# Funciones ###########################


def Limpiar(provval, prodval, defval, cantval, fecval, nrecval):
    provval.set("")
    prodval.set("")
    defval.set("")
    cantval.set("")
    fecval.set("")
    nrecval.set("")


def Guardar(
    proveedor,
    producto,
    defecto,
    cantidad,
    fecha,
    mssgval,
    provval,
    prodval,
    defval,
    cantval,
    fecval,
    nrecval,
    arbol,
):
    mssgval.set("")
    if (
        proveedor == ""
        or producto == ""
        or defecto == ""
        or cantidad == ""
        or fecha == ""
    ):
        mssgval.set("Completa todos los campos arriba de Guardar")
    elif not re.match("^[0-9]+$", cantidad):
        mssgval.set("Cantidad deben ser números.")
        cantval.set("")
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
        Limpiar(provval, prodval, defval, cantval, fecval, nrecval)
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


def Borrar(
    checkval, mssgval, arbol, nrecval, provval, prodval, defval, cantval, fecval
):
    try:
        if checkval == "":
            Limpiar(provval, prodval, defval, cantval, fecval, nrecval)
            mssgval.set("Todo limpio, ingrese N° de reclamo a borrar")
            arbol.delete(*arbol.get_children())
        elif not re.match("^[0-9]+$", checkval):
            mssgval.set("Falta algun número en N° de reclamo")
            nrecval.set("")
        else:
            db = shelve.open("reclamos")
            confirmacion = messagebox.askquestion(
                "Confirmación de borrado",
                "Estas seguro de borrar el reclamo N°" + checkval,
            )
            if confirmacion == "yes":
                del db[checkval]
                mssgval.set("Se ha borrado el reclamo N° " + checkval)
                nrecval.set("")
                db.close
            else:
                mssgval.set("Se ha cancelado borrar el reclamo N° " + checkval)
                nrecval.set("")
                db.close

    except:
        mssgval.set("N° de reclamo no hayado")
        nrecval.set("")


def Modificar(
    proveedor,
    producto,
    defecto,
    cantidad,
    fecha,
    numreclamo,
    mssgval,
    provval,
    prodval,
    defval,
    cantval,
    fecval,
    nrecval,
    arbol,
):
    mssgval.set("")
    try:
        db = shelve.open("reclamos")
        if not re.match("^[0-9]+$", numreclamo):
            mssgval.set("Ingresa N° de reclamo y al menos un campo a modificar.")
            nrecval.set("")
            db.close
        elif db.get(numreclamo, 0) == 0:
            mssgval.set("N° de reclamo no existente")
            nrecval.set("")
            db.close
        elif (
            proveedor == ""
            and producto == ""
            and defecto == ""
            and cantidad == ""
            and fecha == ""
        ):
            mssgval.set("Completar al menos un campo arriba de Guardar")
            nrecval.set("")
            db.close
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
            Limpiar(provval, prodval, defval, cantval, fecval, nrecval)
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
        Limpiar(provval, prodval, defval, cantval, fecval, nrecval)
        db.close


def Listar(mssgval, provval, prodval, defval, cantval, fecval, nrecval, arbol):
    mssgval.set("")
    Limpiar(provval, prodval, defval, cantval, fecval, nrecval)
    mssgval.set("Listando reclamos registrados")
    db = shelve.open("reclamos")
    arbol.delete(
        *arbol.get_children()
    )  # lo que entiendo del splat * aca es que hace unpack de un item sin saber cuantos valores tiene, si lo saco no funciona
    filas = db.get("nreclamo")
    reclist = []
    if filas == None:
        mssgval.set("Faltan cargar datos")
        return filas
    for x in list(range(filas, 0, -1)):
        try:
            if db.get(str(x), 0) == 0:
                continue
            else:
                reclist.append(x)
        except:
            continue
    else:
        contar = 0
        for i in reclist:
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


def Mostrar(numreclamo, mssgval, arbol, nrecval):
    mssgval.set("")
    try:
        if not re.match("^[0-9]+$", numreclamo):
            mssgval.set("Ingresa N° de reclamo a mostrar (solo números).")
            nrecval.set("")
        else:
            arbol.delete(*arbol.get_children())
            db = shelve.open("reclamos")
            try:
                arbol.insert(
                    parent="",
                    index="end",
                    iid=0,
                    text="",
                    values=list(db[numreclamo].values()),
                )
            except:
                mssgval.set("N° de reclamo no encontrado")

            finally:
                nrecval.set("")

            db.close
    except:
        mssgval.set("N° de reclamo no existe")
        nrecval.set("")
        db.close
