import ttkbootstrap as tb
from ttkbootstrap.constants import * 

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

    # BOTONES

    boton1 = tb.Button(frame_botones, text = "Nueva Cita", bootstyle= "success")
    boton1.pack(side=LEFT, padx=5)

    boton2 = tb.Button(frame_botones, text = "Editar Cita", bootstyle= "info")
    boton2.pack(side=LEFT, padx=5)

    boton3 = tb.Button(frame_botones, text = "Eliminar Cita", bootstyle= "danger")
    boton3.pack(side=LEFT, padx=5)

    # FRAME DE LA TABLA A CONTINUACIÓN DE LOS BOTONES

    frame_tabla = tb.Frame(frame)
    frame_tabla.pack(fill= BOTH, expand= True, padx=20, pady= 10)

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

    tabla.column("ID", width= 40)
    tabla.column("Cliente", width=150)
    tabla.column("Fecha", width= 100)
    tabla.column("Hora", width= 80)
    tabla.column("Duración", width= 100)
    tabla.column("Estado", width= 80)

    tabla.pack(fill=BOTH, expand= True)