import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session,Cliente
from components.formularios import agregar_cliente

def vista_clientes(parent):
    # CREAR FRAME PARA CLIENTES
    frame = tb.Frame(parent)
    frame.pack(fill= BOTH, expand= True)

    # TITULO 

    titulo = tb.Label(frame, text ="GESTIÓN DE CLIENTES",font = ("Arial", 20, "bold"))
    titulo.pack(pady= 20)

    # FRAME BOTONES
    frame_botones = tb.Frame(frame)
    frame_botones.pack(fill=X,padx= 20, pady= 20)

    # BOTONES

    boton1 = tb.Button(frame_botones, text = "Nuevo Cliente", command = lambda: agregar_cliente(frame), bootstyle= "success")
    boton1.pack(side=LEFT, padx=5)

    boton2 = tb.Button(frame_botones, text = "Editar Cliente", bootstyle= "info")
    boton2.pack(side=LEFT, padx=5)

    boton3 = tb.Button(frame_botones, text = "Eliminar Cliente", bootstyle= "danger")
    boton3.pack(side=LEFT, padx=5)

    # FRAME DE LA TABLA A CONTINUACIÓN DE LOS BOTONES

    frame_tabla = tb.Frame(frame)
    frame_tabla.pack(fill= BOTH, expand= True, padx=20, pady= 10)

    
    # OBTENER CLIENTES DE LA BD 

    session = Session()
    clientes = session.query(Cliente).all()
    session.close()

    
    # TABLA CLIENTES


    columnas = ("ID","Nombre","Email","Teléfono","Edad","Fecha Registro")
    tabla = tb.Treeview(frame_tabla, columns= columnas, show="headings",height= 15)

    # DEFINIR LOS ENCABEZADOS

    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text ="Nombre")
    tabla.heading("Email", text="Email")
    tabla.heading("Teléfono", text="Teléfono")
    tabla.heading("Edad", text="Edad")
    tabla.heading("Fecha Registro",text="Fecha Registro")

    # ANCHO DE LAS COLUMNAS

    tabla.column("ID", width= 40)
    tabla.column("Nombre", width=150)
    tabla.column("Email", width= 150)
    tabla.column("Teléfono", width= 100)
    tabla.column("Edad", width= 50)
    tabla.column("Fecha Registro", width= 120)

# LLENAR LA TABLA

    for cliente in clientes:
        tabla.insert("", "end", values=(
                    cliente.id,
                    cliente.nombre,
                    cliente.email,
                    cliente.telefono,
                    cliente.edad,
                    cliente.fecha_registro.strftime("%d/%m/%Y")if cliente.fecha_registro else "N/A"))


    tabla.pack(fill=BOTH, expand= True)


    

    # CREAR TABLA 

    



