
def_cajas = ["dc1", "dc2", "dc3", "dc4"]
def_botellas = ["db1", "db2", "db3", "db4"]
def_etiquetas = ["de1", "de2", "de3", "de4"]
def_tapas = ["dt1", "dt2", "dt3", "dt4"]
def_film = ["df1", "df2", "df3", "df4"]
prod_cajas = ["pc1", "pc2", "pc3", "pc4"]
prod_etiquetas = ["pe1", "pe2", "pe3", "pe4"]
prod_tapas = ["pe1", "pe2", "pe3", "pe4"]
prod_botellas = ["pb1", "pb2", "pb3", "pb4"]
prod_film = ["pf1", "pf2", "pf3", "pf4"]

class Proveedor():
    mis_proveedores=[]
    def __init__(self, nombre, productos, defectos):
        self.nombre=nombre
        self.defectos=defectos
        self.productos=productos
        self.__class__.mis_proveedores.append(self)

cartocor = Proveedor("Cartocor", prod_cajas, def_cajas)
cattorini = Proveedor("Cattorini Hnos.", prod_botellas, def_botellas)
multilabel = Proveedor("Multilabel", prod_etiquetas, def_etiquetas)
guala = Proveedor("Guala", prod_tapas, def_tapas)
islagrande = Proveedor("Isla Grande", prod_film, def_film)

nom_prov=[]
runs = 0


def genlist(nom_prov):
    for x in range(len(Proveedor.mis_proveedores)-1, -1, -1):
        nom_prov.append(Proveedor.mis_proveedores[x].nombre)

if runs == 0: 
    genlist(nom_prov)

print(Proveedor.mis_proveedores[1].productos)