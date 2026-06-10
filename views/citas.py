import ttkbootstrap as tb
from ttkbootstrap.constants import *
from database.database import Session,Cita
from components.formularios import agregar_cita, editar_cita

def vista_citas(parent):
    # CREAR FRAME
    frame = tb.Frame(parent)
    frame.pack(fill= BOTH, expand= True)

    # TITULO

    titulo = tb.Label(frame, text= "GESTIÓN DE CITAS", font =("Arial",20,"bold"))
    titulo.pack(pady= 20)

    # FRAME BOTONES

    frame_botones = tb.Frame(frame)
    frame_botones.pack(fill=X, padx=20, pady=20)

    # ELIMINAR CITA
    
    def eliminar_cita():
        # SELECCIONA TUPLA CON LAS ID'S 
        
        seleccion = tabla.selection()

        # VERIFICAR QUE SELCCIONO ALGUNA COSA

        if not seleccion:
            print("Selecciona una cita.")
            return 
        
        # OBTIENE EL ID DE LA CITA 

        cita_id = tabla.item(seleccion[0])["values"][0]

        # ELIMINAR DE LA DB 

        session = Session()
        cita = session.query(Cita).filter_by(id=cita_id).first()

        # BUSCA LA CITA CON EL ID, SI ESTÁ LA ELIMINA 

        if cita:
            session.delete(cita)
            session.commit()
        session.close()

        # ACTUALIZA LA TABLA

        actualizar_tabla()

    def abrir_editar_cita():

        seleccion = tabla.selection()

        if not seleccion:
            print("Selecciona una cita.")
            return 
        
        cita_id = tabla.item(seleccion[0])["values"][0]
        editar_cita(frame,cita_id)

        actualizar_tabla()


    # FRAME DE LA TABLA A CONTINUACIÓN DE LOS BOTONES

    frame_tabla = tb.Frame(frame)
    frame_tabla.pack(fill= BOTH, expand= True, padx=20, pady= 10)

    # OBTENER CLIENTES DE LA BD 

    session = Session()
    citas = session.query(Cita).all()
    

    # TABLA CLIENTES

    columnas = ("ID","Cliente","Fecha","Hora","Duración","Estado")
    tabla = tb.Treeview(frame_tabla, columns= columnas, show="headings",height= 15)

    # DEFINIR LOS ENCABEZADOS

    tabla.heading("ID", text="ID")
    tabla.heading("Cliente", text ="Cliente")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Hora", text="Hora")
    tabla.heading("Duración", text="Duración")
    tabla.heading("Estado",text="Estado")

    # ANCHO DE LAS COLUMNAS

    tabla.column("ID", width= 40, anchor = CENTER)
    tabla.column("Cliente", width=150, anchor = CENTER)
    tabla.column("Fecha", width= 100, anchor = CENTER)
    tabla.column("Hora", width= 80, anchor = CENTER)
    tabla.column("Duración", width= 100, anchor = CENTER)
    tabla.column("Estado", width= 80, anchor = CENTER)

    tabla.pack(fill=BOTH, expand= True)

    # LLENAR LA TABLA

    for cita in citas:
        tabla.insert("", "end", values = (
            cita.id,
            cita.cliente.nombre if cita.cliente else "N/A",
            cita.fecha.strftime("%d/%m/%Y") if cita.fecha else "N/A",
            cita.fecha.strftime("%d/%m/%Y") if cita.fecha else "N/A",
            cita.duracion if cita.duracion else "N/A",
            "Completada" if cita.completada else "Pendiente",
        ))

    session.close()

    def actualizar_tabla():
        for item in tabla.get_children():
            tabla.delete(item)

        session = Session()
        citas = session.query(Cita).all()
        

        for cita in citas:
            tabla.insert("", "end", values = (
                cita.id,
                cita.cliente.nombre if cita.cliente else "N/A",
                cita.fecha.strftime("%d/%m/%Y") if cita.fecha else "N/A",
                cita.fecha.strftime("%H:%M") if cita.fecha else "N/A",
                cita.duracion if cita.duracion else "N/A",
                "Completada" if cita.completada else "Pendiente",
        ))
            
        session.close()
    

    # BOTONES

    boton1 = tb.Button(frame_botones, text="Nueva Cita", command=lambda: agregar_cita(frame), bootstyle="success")
    boton1.pack(side=LEFT, padx=5)

    boton2 = tb.Button(frame_botones, text="Editar Cita", command= abrir_editar_cita,  bootstyle="info")
    boton2.pack(side=LEFT, padx=5)

    boton3 = tb.Button(frame_botones, text="Eliminar Cita", command=eliminar_cita, bootstyle="danger")
    boton3.pack(side=LEFT, padx=5)

    boton4 = tb.Button(frame_botones, text="Actualizar", command=actualizar_tabla, bootstyle="warning")
    boton4.pack(side=LEFT, padx=5)
    
    


