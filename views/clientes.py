import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session,Cliente
from components.formularios import agregar_cliente, editar_cliente, ficha_cliente


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


    def eliminar_cliente():
        
        seleccion = tabla.selection()

        if not seleccion:
            print("Selecciona un cliente.")
            return 
        
        cliente_id = tabla.item(seleccion[0])["values"][0]

        session = Session()
        cliente = session.query(Cliente).filter_by(id=cliente_id).first()
        if cliente:
            session.delete(cliente)
            session.commit()
        session.close()

        actualizar_tabla()

    def abrir_editar_clientes():

        seleccion = tabla.selection()

        if not seleccion:
            print("Selecciona un cliente.")
            return 
        
        cliente_id = tabla.item(seleccion[0])["values"][0]
        editar_cliente(frame,cliente_id)
        actualizar_tabla()


    # BOTONES

    boton1 = tb.Button(frame_botones, text = "Nuevo Cliente", command = lambda: agregar_cliente(frame), bootstyle= "success")
    boton1.pack(side=LEFT, padx=5)

    boton2 = tb.Button(frame_botones, text = "Editar Cliente", command= abrir_editar_clientes,  bootstyle= "info")
    boton2.pack(side=LEFT, padx=5)

    boton3 = tb.Button(frame_botones, text = "Eliminar Cliente", command= eliminar_cliente, bootstyle= "danger")
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

    tabla.column("ID", width= 40, anchor = CENTER)
    tabla.column("Nombre", width=150, anchor = CENTER)
    tabla.column("Email", width= 150, anchor = CENTER)
    tabla.column("Teléfono", width= 100, anchor = CENTER)
    tabla.column("Edad", width= 50, anchor = CENTER)
    tabla.column("Fecha Registro", width= 120, anchor = CENTER)

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

    # BÚSQUEDA CLIENTES

    frame_busqueda = tb.Frame(frame)
    frame_busqueda.pack(fill=X, padx=20, pady=10)

    tb.Label(frame_busqueda, text="Buscar:").pack(side=LEFT, padx=5)
    entry_busqueda = tb.Entry(frame_busqueda, width=30)
    entry_busqueda.pack(side=LEFT, padx=5, fill=X, expand=True)

    def buscar_cliente(event=None):
        termino = entry_busqueda.get().lower()
        for item in tabla.get_children():
            tabla.delete(item)
    
        session = Session()
        clientes = session.query(Cliente).all()
        session.close()
    
        for cliente in clientes:
            if termino in cliente.nombre.lower() or termino in cliente.email.lower():
                tabla.insert("", "end", values=(
                    cliente.id,
                    cliente.nombre,
                    cliente.email,
                    cliente.telefono,
                    cliente.edad,
                    cliente.fecha_registro.strftime("%d/%m/%Y") if cliente.fecha_registro else "N/A"
            ))

    entry_busqueda.bind("<KeyRelease>", buscar_cliente)

    # ACTUALIZAR LA TABLA 

    def  actualizar_tabla():
        for item in tabla.get_children():
            tabla.delete(item)

        session = Session()
        clientes = session.query(Cliente).all()
        session.close()

        for cliente in clientes: 
            tabla.insert("", "end", values =(
                cliente.id,
                cliente.nombre,
                cliente.email,
                cliente.telefono,
                cliente.edad,
                cliente.fecha_registro.strftime("%d/%m/%Y") if cliente.fecha_registro else "N/A"))
                
    boton4 = tb.Button(frame_botones, text = "Actualizar", command = actualizar_tabla, bootstyle= "warning")
    boton4.pack(side=LEFT, padx=5)
            
    
    # PODER ACCEDER AL INTERIOR DE FICHA DE CLIENTES

    def abrir_ficha_cliente(e):
        seleccion = tabla.selection()

        if not seleccion:
            print("Selecciona un cliente.")
            return
        
        cliente_id = tabla.item(seleccion[0])["values"][0]
        ficha_cliente(frame, cliente_id)

    tabla.bind("<Double-1>", abrir_ficha_cliente) 
    
    


    

    



