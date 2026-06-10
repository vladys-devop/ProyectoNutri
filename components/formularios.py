import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session, Cliente, Cita
from datetime import datetime
from tkinter.ttk import Combobox

def agregar_cliente(parent):
    # CREAR VENTANA
    ventana = tb.Toplevel(parent)
    ventana.title("Nuevo Cliente")
    ventana.geometry("400x600")

    # NOMBRE

    label_nombre = tb.Label(ventana, text = "Nombre:")
    label_nombre.pack(pady=5,padx=20,anchor=W)
    entry_nombre = tb.Entry(ventana, width=30)
    entry_nombre.pack(pady=5,padx=20,fill=X)

    # EMAIL

    label_email = tb.Label(ventana, text = "Email:")
    label_email.pack(pady=5,padx=20,anchor=W)
    entry_email = tb.Entry(ventana, width=30)
    entry_email.pack(pady=5,padx=20,fill=X)

    # TELEFONO

    label_telefono = tb.Label(ventana, text = "Telefono:")
    label_telefono.pack(pady=5,padx=20,anchor=W)
    entry_telefono = tb.Entry(ventana, width=30)
    entry_telefono.pack(pady=5,padx=20,fill=X)

    # EDAD

    label_edad = tb.Label(ventana, text = "Edad:")
    label_edad.pack(pady=5,padx=20,anchor=W)
    entry_edad = tb.Entry(ventana, width=30)
    entry_edad.pack(pady=5,padx=20,fill=X)

    # FECHA REGISTRO

    label_peso_inicial = tb.Label(ventana, text = "Peso Inicial:")
    label_peso_inicial.pack(pady=5,padx=20,anchor=W)
    entry_peso_inicial = tb.Entry(ventana, width=30)
    entry_peso_inicial.pack(pady=5,padx=20,fill=X)

    # ALTURA

    label_altura = tb.Label(ventana, text = "Altura:")
    label_altura.pack(pady=5,padx=20,anchor=W)
    entry_altura = tb.Entry(ventana, width=30)
    entry_altura.pack(pady=5,padx=20,fill=X)

    # ALERGIAS

    label_alergias = tb.Label(ventana, text = "Alergias:")
    label_alergias.pack(pady=5,padx=20,anchor=W)
    entry_alergias = tb.Entry(ventana, width=30)
    entry_alergias.pack(pady=5,padx=20,fill=X)

    # INTOLERANCIAS

    label_intolerancias = tb.Label(ventana, text = "Intolerancias:")
    label_intolerancias.pack(pady=5,padx=20,anchor=W)
    entry_intolerancias = tb.Entry(ventana, width=30)
    entry_intolerancias.pack(pady=5,padx=20,fill=X)

    # OBJETIVOS

    label_objetivos = tb.Label(ventana, text = "Objetivos:")
    label_objetivos.pack(pady=5,padx=20,anchor=W)
    entry_objetivos = tb.Entry(ventana, width=30)
    entry_objetivos.pack(pady=5,padx=20,fill=X)


    def guardar_cliente():
        # OBTENER LOS CLIENTES
        nombre = entry_nombre.get()
        email = entry_email.get()
        telefono = entry_telefono.get()
        edad = entry_edad.get()
        peso = entry_peso_inicial.get()
        altura = entry_altura.get()
        alergias = entry_alergias.get()
        intolerancias = entry_intolerancias.get()
        objetivos = entry_objetivos.get()

    # GUARDAR EN LA DB

        session = Session()
        nuevo_cliente = Cliente(
            nombre=nombre,
            email=email,
            telefono = telefono,
            edad=edad,
            peso_inicial = float(peso) if peso else None,
            altura = float(altura) if altura else None,
            alergias = alergias,
            intolerancias = intolerancias,
            objetivos = objetivos,
            fecha_registro = datetime.now()
        )

        session.add(nuevo_cliente)
        session.commit()
        session.close()

        ventana.destroy()


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cliente, bootstyle= "success")
    boton_guardar.pack(pady=20)


def agregar_cita(parent):
    ventana = tb.Toplevel(parent)
    ventana.title("Nueva Cita")
    ventana.geometry("400x600")


    # OBTENER LOS CLIENTES

    session = Session()
    clientes = session.query(Cliente).all()
    session.close()

    nombres_clientes = [cliente.nombre for cliente in clientes]

    # LABEL Y COMBOBOX PARA SELECCIONAR CLIENTES

    label_cliente = tb.Label(ventana, text  = "Cliente:")
    label_cliente.pack(pady= 5, padx= 20, anchor= W)

    combobox_cliente = Combobox(ventana, values =  nombres_clientes, width = 30)
    combobox_cliente.pack(pady = 5, padx= 20, fill = X)

    
    # FECHA 

    label_fecha = tb.Label(ventana, text = "Fecha:")
    label_fecha.pack(pady=5,padx=20,anchor=W)
    entry_fecha = tb.Entry(ventana, width=30)
    entry_fecha.pack(pady=5,padx=20,fill=X)

    # HORA 

    
    label_hora = tb.Label(ventana, text = "Hora:")
    label_hora.pack(pady=5,padx=20,anchor=W)
    entry_hora = tb.Entry(ventana, width=30)
    entry_hora.pack(pady=5,padx=20,fill=X)

    # DURACIÓN: 

    label_duracion = tb.Label(ventana, text = "Duración:")
    label_duracion.pack(pady=5,padx=20,anchor=W)
    entry_duracion = tb.Entry(ventana, width=30)
    entry_duracion.pack(pady=5,padx=20,fill=X)
    
    # NOTAS

    
    label_notas = tb.Label(ventana, text = "Notas:")
    label_notas.pack(pady=5,padx=20,anchor=W)
    entry_notas = tb.Entry(ventana, width=30)
    entry_notas.pack(pady=5,padx=20,fill=X)

    # FUNCIÓN GUARDAR CITAS 

    
    def guardar_cita():
        # OBTENER LAS COTAS
        cliente_nombre = combobox_cliente.get()
        fecha = entry_fecha.get()
        hora = entry_hora.get()
        duracion = entry_duracion.get()
        notas = entry_notas.get()


        # OBTENER EL ID DEL CLIENTE A TRAVÉS DEL NOMBRE

        session = Session()
        cliente = session.query(Cliente).filter_by(nombre = cliente_nombre).first()

        if cliente: 
            fecha_hora = datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")

            nueva_cita = Cita(
                cliente_id = cliente.id,
                fecha = fecha_hora,
                duracion = int(duracion) if duracion else None,
                notas_sesion = notas,
                completada = 0
            )

            session.add(nueva_cita)
            session.commit()

        session.close()
        ventana.destroy()


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cita, bootstyle= "success")
    boton_guardar.pack(pady=20)


def editar_cliente(parent,cliente_id):
    # CREAMOS UNA VENTANA
    ventana = tb.Toplevel(parent)
    ventana.title("Editar Cliente")
    ventana.geometry("400x600")

    # OBTENEMOS EL CLIENTE DE LA BD 

    session = Session()
    cliente = session.query(Cliente).filter_by(id=cliente_id).first()
    session.close()

    if not cliente:
        print("Cliente no encontrado")
        return 
        
    # NOMBRE 

    label_nombre = tb.Label(ventana, text = "Nombre:")
    label_nombre.pack(pady=5, padx= 20, anchor= W)
    entry_nombre = tb.Entry(ventana, width= 30)
    entry_nombre.insert(0,cliente.nombre) # CARGAMOS EL NOMBRE QUE YA TIENE PUESTO EL CLIENTE 
    entry_nombre.pack(pady=5, padx=20, fill= X)

    # EMAIL

    label_email = tb.Label(ventana, text = "Email:")
    label_email.pack(pady=5,padx=20,anchor=W)
    entry_email = tb.Entry(ventana, width=30)
    entry_email.insert(0,cliente.email)
    entry_email.pack(pady=5,padx=20,fill=X)

    # TELEFONO

    label_telefono = tb.Label(ventana, text = "Telefono:")
    label_telefono.pack(pady=5,padx=20,anchor=W)
    entry_telefono = tb.Entry(ventana, width=30)
    entry_telefono.insert(0,cliente.telefono)
    entry_telefono.pack(pady=5,padx=20,fill=X)

    # EDAD

    label_edad = tb.Label(ventana, text = "Edad:")
    label_edad.pack(pady=5,padx=20,anchor=W)
    entry_edad = tb.Entry(ventana, width=30)
    entry_edad.insert(0,cliente.edad)
    entry_edad.pack(pady=5,padx=20,fill=X)

    # FECHA REGISTRO

    label_peso_inicial = tb.Label(ventana, text = "Peso Inicial:")
    label_peso_inicial.pack(pady=5,padx=20,anchor=W)
    entry_peso_inicial = tb.Entry(ventana, width=30)
    entry_peso_inicial.insert(0,cliente.peso_inicial)
    entry_peso_inicial.pack(pady=5,padx=20,fill=X)

    # ALTURA

    label_altura = tb.Label(ventana, text = "Altura:")
    label_altura.pack(pady=5,padx=20,anchor=W)
    entry_altura = tb.Entry(ventana, width=30)
    entry_altura.insert(0,cliente.altura)
    entry_altura.pack(pady=5,padx=20,fill=X)

    # ALERGIAS

    label_alergias = tb.Label(ventana, text = "Alergias:")
    label_alergias.pack(pady=5,padx=20,anchor=W)
    entry_alergias = tb.Entry(ventana, width=30)
    entry_alergias.insert(0,cliente.alergias)
    entry_alergias.pack(pady=5,padx=20,fill=X)

    # INTOLERANCIAS

    label_intolerancias = tb.Label(ventana, text = "Intolerancias:")
    label_intolerancias.pack(pady=5,padx=20,anchor=W)
    entry_intolerancias = tb.Entry(ventana, width=30)
    entry_intolerancias.insert(0,cliente.intolerancias)
    entry_intolerancias.pack(pady=5,padx=20,fill=X)

    # OBJETIVOS

    label_objetivos = tb.Label(ventana, text = "Objetivos:")
    label_objetivos.pack(pady=5,padx=20,anchor=W)
    entry_objetivos = tb.Entry(ventana, width=30)
    entry_objetivos.insert(0,cliente.objetivos)
    entry_objetivos.pack(pady=5,padx=20,fill=X)

    def guardar_cambios():
        # ACTUALIZAMOS LA DB
        session = Session()
        cliente = session.query(Cliente).filter_by(id=cliente_id).first()

        cliente.nombre = entry_nombre.get()
        cliente.email = entry_email.get()
        cliente.telefono = entry_telefono.get()
        cliente.edad = entry_edad.get()
        cliente.peso_inicial = float(entry_peso_inicial.get()) if entry_peso_inicial.get() else None
        cliente.altura = float(entry_altura.get()) if entry_altura.get() else None
        cliente.alergias = entry_alergias.get()
        cliente.intolerancias = entry_intolerancias.get()
        cliente.objetivos = entry_objetivos.get()

        session.commit()
        session.close()
        ventana.destroy()

    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cambios, bootstyle= "success")
    boton_guardar.pack(pady=20)


def editar_cita(parent, cita_id):
    ventana = tb.Toplevel(parent)
    ventana.title("Editar Cita")
    ventana.geometry("400x600")


    # OBTENER LA CITA

    session = Session()
    cita = session.query(Cita).filter_by(id=cita_id).first()
    
    if not cita: 
        print("Cita no encontrada.")
        session.close()
        return 
    

    # GUARDAR NOMBRE ANTES DE CERRAR

    cliente_nombre_actual = cita.cliente.nombre if cita.cliente else ""
    
    # OBTENER CLIENTES

    clientes = session.query(Cliente).all()
    nombres_clientes = [cliente.nombre for cliente in clientes]
    
    session.close()
    
    # CREAR COMBOBOX

    label_cliente = tb.Label(ventana, text="Cliente:")
    label_cliente.pack(pady=5, padx=20, anchor=W)

    combobox_cliente = Combobox(ventana, values=nombres_clientes, width=30)
    combobox_cliente.insert(0, cliente_nombre_actual)
    combobox_cliente.pack(pady=5, padx=20, fill=X)

    
    # FECHA 

    label_fecha = tb.Label(ventana, text = "Fecha:")
    label_fecha.pack(pady=5,padx=20,anchor=W)
    entry_fecha = tb.Entry(ventana, width=30)
    entry_fecha.insert(0,cita.fecha.strftime("%d/%m/%Y"))
    entry_fecha.pack(pady=5,padx=20,fill=X)

    # HORA 

    
    label_hora = tb.Label(ventana, text = "Hora:")
    label_hora.pack(pady=5,padx=20,anchor=W)
    entry_hora = tb.Entry(ventana, width=30)
    entry_hora.insert(0,cita.fecha.strftime("%H:%M"))
    entry_hora.pack(pady=5,padx=20,fill=X)

    # DURACIÓN: 

    label_duracion = tb.Label(ventana, text = "Duración:")
    label_duracion.pack(pady=5,padx=20,anchor=W)
    entry_duracion = tb.Entry(ventana, width=30)
    entry_duracion.insert(0,cita.duracion)
    entry_duracion.pack(pady=5,padx=20,fill=X)
    
    # NOTAS

    
    label_notas = tb.Label(ventana, text = "Notas:")
    label_notas.pack(pady=5,padx=20,anchor=W)
    entry_notas = tb.Entry(ventana, width=30)
    entry_notas.insert(0,cita.notas_sesion)
    entry_notas.pack(pady=5,padx=20,fill=X)

    def guardar_cambios():
        session = Session()
        cita = session.query(Cita).filter_by(id=cita_id).first()

        # OBTENEMOS EL CLIEJNTE POR EL NOMBRE
        cliente_nombre = combobox_cliente.get()
        cliente = session.query(Cliente).filter_by(nombre = cliente_nombre).first()

        if cliente: 
            fecha_hora = datetime.strptime(f"{entry_fecha.get()} {entry_hora.get()}", "%d/%m/%Y %H:%M")
            cita.cliente_id = cliente.id
            cita.fecha = fecha_hora 
            cita.duracion = int(entry_duracion.get()) if entry_duracion.get() else None
            cita.notas_sesion = entry_notas.get()

            session.commit()
        
        session.close()
        ventana.destroy()


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cambios, bootstyle= "success")
    boton_guardar.pack(pady=20)



def ficha_cliente(parent, cliente_id):
    # CREAMOS LA VENTANA
    ventana = tb.Toplevel(parent)
    ventana.title("Ficha del Cliente")
    ventana.geometry("700x600")

    # OBTENEMOS EL CLIENTE

    session = Session()
    cliente = session.query(Cliente).filter_by(id = cliente_id).first()
    session.close()

    if not cliente:
        print("Cliente no encontrado.")
        return
    
    # CREAR NOTEBOOK 
    notebook = tb.Notebook(ventana)
    notebook.pack(fill=BOTH, expand=True,padx=10, pady=10)

    # 1. INFORMACION 

    tab_info = tb.Frame(notebook)
    notebook.add(tab_info, text="Información")

    tb.Label(tab_info, text=f"Nombre: {cliente.nombre}", font=("Arial",12)).pack(pady=10)
    tb.Label(tab_info, text=f"Email: {cliente.email}", font = ("Arial",12)).pack(pady=10)
    tb.Label(tab_info,text= f"Teléfono: {cliente.telefono}", font = ("Arial",12)).pack(pady=10)
    tb.Label(tab_info,text= f"Edad: {cliente.edad}", font = ("Arial",12)).pack(pady=10)
    tb.Label(tab_info,text= f"Peso: {cliente.peso_inicial}", font = ("Arial",12)).pack(pady=10)
    tb.Label(tab_info,text= f"Altura: {cliente.altura}", font = ("Arial",12)).pack(pady=10)

    # 2. DIETA
    tab_dieta = tb.Frame(notebook)
    notebook.add(tab_dieta,text = "Dieta")
    tb.Label(tab_dieta, text = "Archivo Dieta", font= ("Arial",14)).pack(pady= 20)

    # 3. CITAS
    tab_citas = tb.Frame(notebook)
    notebook.add(tab_citas, text="Citas")
    tb.Label(tab_citas, text ="Citas del Cliente",font=("Arial",14)).pack(pady=20)


