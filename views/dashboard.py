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
    tarjeta1 = tb.Labelframe(frame_tarjetas, text = "Total Clientes", bootstyle= "info")
    tarjeta1.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta1, text = str(total_clientes), font = ("Arial",32,"bold"), bootstyle= "info").pack(pady= 20)

    # TARJETA TOTAL CITAS
    tarjeta2 = tb.Labelframe(frame_tarjetas, text = "Total Citas", bootstyle= "success")
    tarjeta2.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta2, text = str(total_citas), font = ("Arial",32,"bold"), bootstyle= "success").pack(pady= 20)

    # TARJETA CITAS HOY
    tarjeta3 = tb.Labelframe(frame_tarjetas, text = "Citas Hoy", bootstyle= "warning")
    tarjeta3.pack(side= LEFT, fill= BOTH, expand= True, padx= 10, pady= 10)
    tb.Label(tarjeta3, text = str(citas_hoy), font = ("Arial",32,"bold"), bootstyle= "warning").pack(pady= 20)

    # INFORMACIÓN 
    frame_info = tb.Labelframe(frame, text="Información",bootstyle= "light")
    frame_info.pack(fill= BOTH, expand= True, padx= 20, pady= 20)

    info_text = "Bienvenido a la app de gestión nutricional.\n\nUsa el menú para navegar."
    tb.Label(frame_info, text= info_text, justify="left", font = ("Arial", 11)).pack(fill=BOTH, expand= True, padx= 20, pady= 20)
    
    