import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session,Cliente,Cita
from datetime import *




def vista_dashboard(parent):
    # CREAR FRAME DENTRO CONTENEDOR 
    frame = tb.Frame(parent)
    frame.pack(fill= BOTH, expand = True)

    # CONTAR CITAS TOTALES Y CLIENTES

    session = Session()
    total_clientes = session.query(Cliente).count()
    total_citas = session.query(Cita).count()

    # CITAS DE HOY 

    hoy = date.today()
    citas_hoy = session.query(Cita).filter(
        Cita.fecha >= datetime(hoy.year, hoy.month, hoy.day),
        Cita.fecha < datetime(hoy.year, hoy.month, hoy.day) + timedelta(days=1)).count() 
    session.close()

    
    # AGREGAR TÍTULO 
    titulo = tb.Label(frame, text = "DASHBOARD", font = ("Arial",20,"bold"))
    titulo.pack(pady= 20)

    # TARJETAS 
    frame_tarjetas = tb.Frame(frame)
    frame_tarjetas.pack(fill= X, padx= 20, pady= 20)

    # TARJETA CLIENTES
    tarjeta1 = tb.Labelframe(frame_tarjetas, text = "TOTAL CLIENTES", bootstyle= "info")
    tarjeta1.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta1, text = str(total_clientes), font = ("Arial",32,"bold"), bootstyle= "info").pack(pady= 20)

    # TARJETA TOTAL CITAS
    tarjeta2 = tb.Labelframe(frame_tarjetas, text = "TOTAL CITAS", bootstyle= "success")
    tarjeta2.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta2, text = str(total_citas), font = ("Arial",32,"bold"), bootstyle= "success").pack(pady= 20)

    # TARJETA CITAS HOY
    tarjeta3 = tb.Labelframe(frame_tarjetas, text = "CITAS HOY", bootstyle= "warning")
    tarjeta3.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta3, text = str(citas_hoy), font = ("Arial",32,"bold"), bootstyle= "warning").pack(pady= 20)

    # INFORMACIÓN 
    frame_info = tb.Labelframe(frame, text="PRÓXIMAS CITAS",bootstyle= "light")
    frame_info.pack(fill= BOTH, expand= True, padx= 20, pady= 20)

    # TABLA CITAS

    frame_tabla_citas = tb.Frame(frame_info)
    frame_tabla_citas.pack(fill=BOTH,expand=True, padx=10,pady=10)

    columnas_citas = ("Cliente", "Fecha","Hora","Duración")
    tablas_citas = tb.Treeview(frame_tabla_citas,columns=columnas_citas,show="headings")

    tablas_citas.heading("Cliente", text="Cliente")
    tablas_citas.heading("Fecha",text="Fecha")
    tablas_citas.heading("Hora",text="Hora")
    tablas_citas.heading("Duración", text="Duración")
    
    tablas_citas.column("Cliente", width= 150, anchor="center")
    tablas_citas.column("Fecha", width=100, anchor="center")
    tablas_citas.column("Hora",width=80,anchor="center")
    tablas_citas.column("Duración",width=80,anchor="center")

    # OBTENER LAS PRÓXIMAS CITAS ORDENADAS

    session_citas = Session()
    citas_proximas = session.query(Cita).filter(Cita.fecha >= datetime.now()).order_by(Cita.fecha).limit(5).all()

    for cita in citas_proximas:
        tablas_citas.insert("","end",values =(
            cita.cliente.nombre if cita.cliente else "N/A",
            cita.fecha.strftime("%d.%m.%Y"),
            cita.fecha.strftime("%H:%M"),
            f"{cita.duracion}min" if cita.duracion else "N/A",

        ))

    session_citas.close()
    tablas_citas.pack(fill=BOTH, expand = True)


    
    
    