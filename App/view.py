from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Button
from tkinter import Frame
from tkinter import Scrollbar
from tkinter import ttk
from tkinter.font import Font
from model import ABMC
from tkcalendar import DateEntry


def ventana_ppal(root):
    root.resizable(False, False)
    root.title("Reclamos a Proveedores")
    root.configure(background="khaki")
    # root.iconbitmap("pngwing.ico")
    b_font = Font(family="Helvetica", size=11, weight="bold")
    b_font2 = Font(family="Helvetica", size=10, weight="bold")

    # Definicion de variables #############################
    #######################################################

    provval, prodval, defval, cantval, fecval, nrecval, mssgval = (
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
    )

    def_cajas = [
        "curvas",
        "deslaminadas",
        "error de impresión",
        "error paletizado",
        "humedas/mojadas",
    ]

    def_botellas = [
        "dimensiones fuera de especificación",
        "lamparones",
        "espejadas",
        "weathering",
        "paletizado dañado/hardboard",
        "vidrio fino",
        "contaminación",
        "error palletizado",
    ]

    def_etiquetas = [
        "liner dañado",
        "error de impresión",
        "mal bobinado",
        "error de identificación",
        "no despega",
        "textos desactulizados",
    ]

    def_tapas = [
        "error impresión",
        "medidas fuera de especificación",
        "falta componente",
        "rotas",
        "inserto suelto",
        "golpeadas",
        "contaminación",
    ]

    def_film = ["corta film", "contaminación", "distribución no uniforme"]

    prod_cajas = [
        "Caja FB 12/75 cl",
        "Caja CB 6/70 cl",
        "Caja BM 6/75 cl",
        "Caja FB 12/45 cl",
        "Caja Ser Trad 12/70 cl",
        "Caja PEM 6/75 cl" "Caja Carpano Rosso" "Caja Carpano Bianco",
    ]
    prod_botellas = [
        "Bot. FB/BM 75 cl",
        "Bot. FB/BM 45 cl",
        "Bot. CB/BM 70 cl",
        "Bot PEM 75 cl",
        "Bot Carpano 95 cl",
        "Bot Sernova 70 cl",
        "Bot FB/BM/PEM 5 cl",
        "Bot CB 5 cl",
    ]
    prod_etiquetas = [
        "Etiq. FB 75 cl",
        "C/Etiq. FB 75 cl",
        "Etiq. FB 45 cl",
        "C/Etiq. FB 45 cl",
        "Etiq. CB 70 cl",
        "C/Etiq. CB 05 cl",
        "Etiq. BM 75 cl",
        "C/Etiq. BM 75 cl",
        "Etiq. BM 45 cl",
        "C/Etiq. BM 45 cl",
        "Etiq. FB 5 cl",
        "C/Etiq. FB 5 cl",
    ]
    prod_tapas = [
        "Tapa FB 75/100 cl",
        "Tapa PEM 75 cl",
        "Tapa Carpano Rosso",
        "Tapa Carpano Bianco",
        "Tapon Sernova",
        "Tapa BM 75 cl",
        "Tapa FB 45 cl",
        "Tapa BM 45 cl",
        "Tapa PEM 5 cl",
        "Tapa FB 5 cl",
    ]

    prod_film = ["film envolvedora", "film manual", "film techo pallet"]

    # Definicion de Proveedores ###########################
    #######################################################

    class Proveedor:
        nombre = ""
        defectos = ""
        productos = ""
        mis_proveedores = []
        nom_provs = []

        def __init__(self, nombre, productos, defectos):
            self.nombre = nombre
            self.defectos = defectos
            self.productos = productos
            self.__class__.mis_proveedores.append(self)

        @classmethod
        def listnomprov(self):
            for x in range(0, len(self.mis_proveedores), 1):
                self.nom_provs.append(self.mis_proveedores[x].nombre)

    cartocor = Proveedor("Cartocor", prod_cajas, def_cajas)
    multilabel = Proveedor("Multilabel", prod_etiquetas, def_etiquetas)
    guala = Proveedor("Guala", prod_tapas, def_tapas)
    cattorini = Proveedor("Cattorini Hnos.", prod_botellas, def_botellas)
    islagrande = Proveedor("Isla Grande", prod_film, def_film)

    # Variables para manejar los desplegables #############
    #######################################################

    firstrun = 0

    # Funciones auxiliares para la interfaz ###############
    #######################################################

    if firstrun == 0:
        Proveedor.listnomprov()
        firstrun += 1

    def elijeprov(event):
        for x in range(0, len(Proveedor.mis_proveedores), 1):
            if Proveedor.mis_proveedores[x].nombre == e_proveedor.get():
                e_defecto.config(values=Proveedor.mis_proveedores[x].defectos)
                e_producto.config(values=Proveedor.mis_proveedores[x].productos)
                e_defecto.current(0)
                e_producto.current(0)

    def elijeprod(*args):
        for x in range(0, len(Proveedor.mis_proveedores), 1):
            if Proveedor.mis_proveedores[x].nombre == e_proveedor.get():
                e_defecto.config(values=Proveedor.mis_proveedores[x].defectos)
                e_producto.config(values=Proveedor.mis_proveedores[x].productos)

    # label titulo principal ##############################
    #######################################################

    t_principal = Label(
        root, text="Registro de Reclamos a Proveedores", bg="khaki", font=b_font2
    )
    t_principal.grid(row=0, columnspan=6, pady=10)

    # labels de campos ####################################
    #######################################################

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

    fila7 = Label(
        root, textvariable=mssgval, bg="khaki", font=b_font2
    )  # label de notificaciones
    fila7.grid(row=10, column=4, columnspan=2, sticky="n")

    # Entries #############################################
    #######################################################

    e_proveedor = ttk.Combobox(
        root,
        values=Proveedor.nom_provs,
        width=18,
        textvariable=provval,
        state="readonly",
    )
    e_proveedor.grid(row=1, column=1, padx=10, pady=3)
    e_proveedor.bind("<<ComboboxSelected>>", elijeprov)
    e_proveedor.current(0)

    e_producto = ttk.Combobox(
        root,
        values=prod_cajas,
        width=18,
        textvariable=prodval,
        state="readonly",
    )
    e_producto.grid(row=2, column=1, padx=10, pady=3)

    e_producto.current(0)

    e_defecto = ttk.Combobox(
        root,
        values=def_cajas,
        width=18,
        textvariable=defval,
        state="readonly",
    )

    e_defecto.current(0)
    e_defecto.grid(row=3, column=1, padx=10, pady=3)

    e_cantidad = Entry(root, textvariable=cantval, bg="white")
    e_cantidad.grid(row=4, column=1, padx=10, pady=3)

    e_fecha = DateEntry(
        root,
        selectmode="day",
        bg="white",
        width=18,
        date_pattern="dd/MM/yyyy",
        textvariable=fecval,
    )
    e_fecha.grid(row=5, column=1, padx=10, pady=3)

    e_nreclamo = Entry(root, textvariable=nrecval, bg="white")
    e_nreclamo.grid(row=8, column=1, padx=10, pady=3)

    prodval.trace_add("write", elijeprod)

    # Stilo del Treeview ##################################
    #######################################################

    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "Treeview",
        background="lightgoldenrod3",
        foreground="black",
        rowheight=20,
        fieldbackground="lightgoldenrod3",
    )

    style.map("Treeview", background=[("selected", "khaki4")])

    # Treeview Frame ######################################
    #######################################################

    m_arbol = Frame(root)
    m_arbol.grid(row=1, rowspan=9, column=4, padx=5, pady=4, sticky="n")

    # Treeview Scrollbar ##################################
    #######################################################

    scroll_arbol = Scrollbar(m_arbol)
    scroll_arbol.pack(side="right", fill="y")

    # Treeview ############################################
    #######################################################

    arbol = ttk.Treeview(m_arbol, yscrollcommand=scroll_arbol.set)
    arbol["columns"] = ("N°", "Fecha", "Proveedor", "Producto", "Defecto", "Cantidad")

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

    arbol.pack()

    scroll_arbol.config(command=arbol.yview)

    # Instanciación #######################################
    #######################################################

    boton = ABMC(mssgval, arbol, nrecval, provval, prodval, defval, cantval, fecval)

    # Botones #############################################
    #######################################################

    b_guardar = Button(
        root,
        text="Guardar",
        borderwidth=4,
        command=lambda: boton.Guardar(),
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
        command=lambda: boton.Mostrar(),
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
        command=lambda: boton.Modificar(),
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
        command=lambda: boton.Borrar(),
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
        command=lambda: boton.Listar(),
        fg="black",
        bg="gold2",
        width=10,
        font=b_font,
    )
    b_listar.grid(row=9, column=0, pady=3, padx=5)