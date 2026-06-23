import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session, Cliente, Cita, Dieta, Evolucion
from datetime import datetime
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tempfile
import re
from tkinter import messagebox



"""
Módulo de formularios.
Contiene funciones para agregar y editar clientes, citas, dietas  y evoluciones. 
"""



# VALIDACIONES 

def validar_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(regex, email) is not None

def validar_campos_cliente(nombre,email,telefono):
    if not nombre or not nombre.strip():
        return False, "El nombre es obligatorio"
    
    if not email or not email.strip():
        return False, "El email es obligatorio"
    
    if not validar_email(email):
        return False, "Formato de email inválido."
    
    if telefono and not telefono.isdigit():
        return False, "El teléfono solo puede contener números."
    
    return True, "OK"

def validar_campos_cita(cliente_nombre,fecha,hora,duracion):
    if not cliente_nombre or not cliente_nombre.strip():
        return False, "Debes de seleccionar un cliente"
    
    if not fecha or not fecha.strip():
        return False, "La fecha es obligatoria"
    
    if not hora or not hora.strip():
        return False, "La hora es obligatoria"
    
    if duracion and not duracion.isdigit():
        return False, "La duración tiene que ser un número"
    
    return True, "OK"

# CREAR VENTANA
def agregar_cliente(parent):
    ventana = tb.Toplevel(parent)
    ventana.title("Nuevo Cliente")
    ventana.geometry("400x700")

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

        # VALIDAR LOS DATOS

        valido, mensaje = validar_campos_cliente(nombre,email,telefono)
        if not valido: 
            messagebox.showwarning("Cuidado",mensaje)
            return

        try:
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
            messagebox.showinfo("Éxito","Cliente guardado correctamente")

            ventana.destroy()
        
        except Exception as e:
            messagebox.showerror("Error",f"Error al guardar: {e}")


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cliente, bootstyle= "success")
    boton_guardar.pack(pady=20)


def agregar_cita(parent):
    ventana = tb.Toplevel(parent)
    ventana.title("Nueva Cita")
    ventana.geometry("400x700")


    # OBTENER LOS CLIENTES
    try:

        session = Session()
        clientes = session.query(Cliente).all()
        session.close()
        nombres_clientes = [cliente.nombre for cliente in clientes]
    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener los clientes: {e}")
        ventana.destroy()
        return

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

        # VALIDAR LOS CAMPOS 

        valido, mensaje = validar_campos_cita(cliente_nombre, fecha,hora,duracion)
        if not valido:
            messagebox.showwarning("Cuidado", mensaje)
            return


        # OBTENER EL ID DEL CLIENTE A TRAVÉS DEL NOMBRE
        try:
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
            messagebox.showinfo("Éxito","Cita guardada correctamente.")
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error",f"Error al guardar la cita: {e}")


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cita, bootstyle= "success")
    boton_guardar.pack(pady=20)


def editar_cliente(parent,cliente_id):
    # CREAMOS UNA VENTANA
    ventana = tb.Toplevel(parent)
    ventana.title("Editar Cliente")
    ventana.geometry("400x700")

    # OBTENEMOS EL CLIENTE DE LA BD 
    try:
        session = Session()
        cliente = session.query(Cliente).filter_by(id=cliente_id).first()
        session.close()

        if not cliente:
            print("Cliente no encontrado")
            return 
    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener cliente: {e}")
        ventana.destroy()
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
        try:

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
        except Exception as e:
            messagebox.showerror("Error",f"Error al guardar el cambio: {e}")

    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cambios, bootstyle= "success")
    boton_guardar.pack(pady=20)


def editar_cita(parent, cita_id):
    ventana = tb.Toplevel(parent)
    ventana.title("Editar Cita")
    ventana.geometry("400x700")


    # OBTENER LA CITA
    try:
        session = Session()
        cita = session.query(Cita).filter_by(id=cita_id).first()
        
        if not cita: 
            messagebox.showwarning("Cuidado","Cita no encontrada")
            session.close()
            ventana.destroy()
            return 
    

        # GUARDAR NOMBRE ANTES DE CERRAR

        cliente_nombre_actual = cita.cliente.nombre if cita.cliente else ""
    
        # OBTENER CLIENTES

        clientes = session.query(Cliente).all()
        nombres_clientes = [cliente.nombre for cliente in clientes]
    
        session.close()
    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener la cita: {e}")
        ventana.destroy()
        return 
    
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
        try:
            session = Session()
            cita = session.query(Cita).filter_by(id=cita_id).first()

            # OBTENEMOS EL CLIEJNTE POR EL NOMBRE
            cliente_nombre = combobox_cliente.get()
            cliente = session.query(Cliente).filter_by(nombre = cliente_nombre).first()

            if cliente: 
                fecha_hora = datetime.strptime(f"{entry_fecha.get()} {entry_hora.get()}", "%d.%m.%Y %H:%M")
                cita.cliente_id = cliente.id
                cita.fecha = fecha_hora 
                cita.duracion = int(entry_duracion.get()) if entry_duracion.get() else None
                cita.notas_sesion = entry_notas.get()

                session.commit()
                messagebox.showinfo("Éxito","Cita actualizada correctamente.")
        
            session.close()
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error",f"Error al guardar los cambios: {e}")


    # BOTÓN DE GUARDAR
    boton_guardar = tb.Button(ventana, text="Guardar", command= guardar_cambios, bootstyle= "success")
    boton_guardar.pack(pady=20)



def ficha_cliente(parent, cliente_id):
    # CREAMOS LA VENTANA
    ventana = tb.Toplevel(parent)
    ventana.title("Ficha del Cliente")
    ventana.geometry("700x600")

    # OBTENEMOS EL CLIENTE
    try:
        session = Session()
        cliente = session.query(Cliente).filter_by(id = cliente_id).first()
        session.close()

        if not cliente:
            messagebox.showwarning("Cuidado","Cliente no encontrado")
            return
    
    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener cliente: {e}")
        ventana.destroy()
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
    notebook.add(tab_dieta, text="Dieta")

    # TABLA DIETAS
    frame_tabla_dietas = tb.Frame(tab_dieta)
    frame_tabla_dietas.pack(fill=BOTH, expand=True, padx=20, pady=10)

    columnas_dieta = ("ID", "Nombre", "Fecha")
    tabla_dietas = tb.Treeview(frame_tabla_dietas, columns=columnas_dieta, show="headings", height=10)

    tabla_dietas.heading("ID", text="ID")
    tabla_dietas.heading("Nombre", text="Nombre")
    tabla_dietas.heading("Fecha", text="Fecha")

    tabla_dietas.column("ID", width=40, anchor="center")
    tabla_dietas.column("Nombre", width=150, anchor="center")
    tabla_dietas.column("Fecha", width=120, anchor="center")

    # LLENAR TABLA CON DIETAS DEL CLIENTE

    try:
        session_dieta = Session()
        dietas = session_dieta.query(Dieta).filter_by(cliente_id=cliente_id).all()
        for dieta in dietas:
            tabla_dietas.insert("", "end", values=(
                dieta.id,
                dieta.nombre,
                dieta.fecha.strftime("%d/%m/%Y") if dieta.fecha else "N/A"
            ))
        session_dieta.close()
    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener dietas: {e}")


    tabla_dietas.pack(fill=BOTH, expand=True)

    # BOTONES
    frame_botones_dieta = tb.Frame(tab_dieta)
    frame_botones_dieta.pack(fill=X, padx=20, pady=10)

    def agregar_dieta():
        
        try:
            archivo = askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if archivo:
                nombre = os.path.basename(archivo).replace(".pdf", "")
                with open(archivo, "rb") as f:
                    contenido = f.read()
                
                session_add = Session()
                nueva_dieta = Dieta(
                    cliente_id=cliente_id,
                    nombre=nombre,
                    fecha=datetime.now(),
                    archivo=contenido
                )
                session_add.add(nueva_dieta)
                session_add.commit()
                session_add.close()
                
                actualizar_tabla_dietas()
                messagebox.showinfo("Éxito","Dieta agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error",f"Error al agregar dieta: {e}")

    def abrir_dieta():
        try:
            seleccion = tabla_dietas.selection()
            if not seleccion:
                messagebox.showwarning("Cuidado","Selecciona una dieta.")
                return
            
            dieta_id = tabla_dietas.item(seleccion[0])["values"][0]
            session_open = Session()
            dieta = session_open.query(Dieta).filter_by(id=dieta_id).first()
            if dieta and dieta.archivo:
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
                    f.write(dieta.archivo)
                    os.startfile(f.name)
            session_open.close()
        except Exception as e:
            messagebox.showerror("Error",f"Error al abrir dieta: {e}")


    def descargar_dieta():
        try:
            seleccion = tabla_dietas.selection()
            if not seleccion:
                messagebox.showwarning("Cuidado","Selecciona una dieta.")
                return
        
            dieta_id = tabla_dietas.item(seleccion[0])["values"][0]
            session_down = Session()
            dieta = session_down.query(Dieta).filter_by(id=dieta_id).first()
            if dieta and dieta.archivo:
                archivo = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if archivo:
                    with open(archivo, "wb") as f:
                        f.write(dieta.archivo)
            session_down.close()
        
        except Exception as e:
            messagebox.showerror("Error",f"Error al descargar: {e}")

    def eliminar_dieta():
        try:
            seleccion = tabla_dietas.selection()
            if not seleccion:
                messagebox.showwarning("Cuidado","Selecciona una dieta.")
                return
            
            dieta_id = tabla_dietas.item(seleccion[0])["values"][0]
            session_del = Session()
            dieta = session_del.query(Dieta).filter_by(id=dieta_id).first()
            if dieta:
                session_del.delete(dieta)
                session_del.commit()
            session_del.close()
            actualizar_tabla_dietas()
        
        except Exception as e: 
            messagebox.showerror("Error",f"Error al eliminar: {e}")



    def actualizar_tabla_dietas():
        try:
            for item in tabla_dietas.get_children():
                tabla_dietas.delete(item)
            
            session_upd = Session()
            dietas = session_upd.query(Dieta).filter_by(cliente_id=cliente_id).all()
            for dieta in dietas:
                tabla_dietas.insert("", "end", values=(
                    dieta.id,
                    dieta.nombre,
                    dieta.fecha.strftime("%d/%m/%Y") if dieta.fecha else "N/A"
                ))
            session_upd.close()

        except Exception as e:
            messagebox.showerror("Error",f"Error al actualizar: {e}")


    boton_agregar_dieta = tb.Button(frame_botones_dieta, text="Agregar Dieta", command=agregar_dieta, bootstyle="success")
    boton_agregar_dieta.pack(side=LEFT, padx=5)
    boton_abrir_dieta = tb.Button(frame_botones_dieta, text="Abrir", command=abrir_dieta, bootstyle="info")
    boton_abrir_dieta.pack(side=LEFT, padx=5)

    boton_descargar_dieta = tb.Button(frame_botones_dieta, text="Descargar", command=descargar_dieta, bootstyle="warning")
    boton_descargar_dieta.pack(side=LEFT, padx=5)

    boton_eliminar_dieta = tb.Button(frame_botones_dieta, text="Eliminar", command=eliminar_dieta, bootstyle="danger")
    boton_eliminar_dieta.pack(side=LEFT, padx=5)


    # 3. CITAS
    tab_citas = tb.Frame(notebook)
    notebook.add(tab_citas, text="Citas")

    # TABLA CITAS

    frame_tabla_citas_cliente = tb.Frame(tab_citas)
    frame_tabla_citas_cliente.pack(fill=BOTH, expand=True,padx=20,pady=10)
    
    columnas_citas_cliente = ("ID","Fecha","Hora","Duración","Notas")
    tabla_citas_cliente = tb.Treeview(frame_tabla_citas_cliente, columns= columnas_citas_cliente,show="headings",height=10)

    tabla_citas_cliente.heading("ID", text ="ID")
    tabla_citas_cliente.heading("Fecha", text="Fecha")
    tabla_citas_cliente.heading("Hora", text="Hora")
    tabla_citas_cliente.heading("Duración", text="Duración")
    tabla_citas_cliente.heading("Notas", text="Notas")


    tabla_citas_cliente.column("ID",width= 40, anchor="center")
    tabla_citas_cliente.column("Fecha",width= 100, anchor="center")
    tabla_citas_cliente.column("Hora",width= 80, anchor="center")
    tabla_citas_cliente.column("Duración",width= 80, anchor="center")
    tabla_citas_cliente.column("Notas",width= 200, anchor="w")

    # OBTENER LAS CITAS DEL CLIENTE
    try:
        session_citas_cliente =  Session()
        citas_cliente = session_citas_cliente.query(Cita).filter_by(cliente_id = cliente_id).order_by(Cita.fecha).all()

        for cita in citas_cliente:
            tabla_citas_cliente.insert("","end", values=(
                cita.id,
                cita.fecha.strftime("%d.%m.%Y") if cita.fecha else "N/A",
                cita.fecha.strftime("%H:%M") if cita.fecha else "N/A",
                f"{cita.duracion} min" if cita.duracion else "N/A",
                cita.notas_sesion if cita.notas_sesion else "No hay notas."
            ))


        session_citas_cliente.close()
    
    except Exception as e: 
        messagebox.showwarning("Error",f"Error al obtener citas: {e}")

    tabla_citas_cliente.pack(fill=BOTH, expand= True)                        
    tb.Label(tab_citas, text ="Citas del Cliente",font=("Arial",14)).pack(pady=20)
    

    # 4. EVOLUCIÓN 

    tab_evolucion = tb.Frame(notebook)
    notebook.add(tab_evolucion, text ="Evolución")

    # TABLA DE EVOLUCIÓN
    frame_tabla_evolucion = tb.Frame(tab_evolucion)
    frame_tabla_evolucion.pack(fill= BOTH, expand = True, padx=20, pady=10)

    columnas_evo = ("ID","Fecha","Peso (KG)","Notas")
    tabla_evolucion = tb.Treeview(frame_tabla_evolucion,columns=columnas_evo,show = "headings", height=10)

    tabla_evolucion.heading("ID",text="ID")
    tabla_evolucion.heading("Fecha", text="Fecha")
    tabla_evolucion.heading("Peso (KG)",text="Peso (KG)")
    tabla_evolucion.heading("Notas", text="Notas")

    tabla_evolucion.column("ID",width=40,anchor="center")
    tabla_evolucion.column("Fecha",width=100,anchor="center")
    tabla_evolucion.column("Peso (KG)",width=80,anchor="center")
    tabla_evolucion.column("Notas",width=200,anchor="w")

    # OBTENER EVOLUCIÓN

    try: 

        session_evo = Session()
        evolucion = session_evo.query(Evolucion).filter_by(cliente_id = cliente_id) .order_by(Evolucion.fecha.desc()).all()

        for evo in evolucion: 
            tabla_evolucion.insert("", "end", values =(
                evo.id,
                evo.fecha.strftime("%d.%m.%Y") if evo.fecha else "N/A",
                evo.peso if evo.peso else "N/A",
                evo.notas if evo.notas else "No hay notas."
            ))

        session_evo.close()

    except Exception as e:
        messagebox.showerror("Error",f"Error al obtener evolución: {e}")

    tabla_evolucion.pack(fill=BOTH,expand=True)

    # BOTONES 
    frame_botones_evo = tb.Frame(tab_evolucion)
    frame_botones_evo.pack(fill=X, padx=20,pady=10)

    def agregar_evolucion():
        ventana_evo = tb.Toplevel(ventana)
        ventana_evo.title("Nueva Evolución")
        ventana_evo.geometry("400x300")

        tb.Label(ventana_evo, text ="Peso (KG):").pack(padx=20,pady=5,anchor=W)
        entry_peso = tb.Entry(ventana_evo,width=30)
        entry_peso.pack(pady=5,padx=20,fill=BOTH,expand=True)

        tb.Label(ventana_evo,text="Notas:").pack(pady=5,padx=20,anchor=W)
        text_notas = tb.Text(ventana_evo,height=6,width=40)
        text_notas.pack(pady=5,padx=20,fill=BOTH,expand=True)

        def guardar_evo():
            peso = entry_peso.get()
            notas = text_notas.get("1.0", "end-1c")

            if not peso:
                messagebox.showwarning("Cuidado","Ingresa el peso.")
                return
            
            try:
                session_add_evo = Session()
                nueva_evo = Evolucion(cliente_id = cliente_id, fecha = datetime.now(), peso = float(peso), notas = notas)


                session_add_evo.add(nueva_evo)
                session_add_evo.commit()
                session_add_evo.close()

                actualizar_tabla_evolucion()
                ventana_evo.destroy()

            except Exception as e:
                messagebox.showerror("Error",f"Error al guardar: {e}")
            


        boton_guardar = tb.Button(ventana_evo, text="Guardar", command = guardar_evo, bootstyle= "success")
        boton_guardar.pack(pady=20)

    def actualizar_tabla_evolucion():
        try:
            for item in tabla_evolucion.get_children():
                tabla_evolucion.delete(item)

            session_up_evo = Session()
            evolucion = session_up_evo.query(Evolucion).filter_by(cliente_id=cliente_id).order_by(Evolucion.fecha.desc()).all()
            for evo in evolucion:
                tabla_evolucion.insert("", "end",values=(
                    evo.id,
                    evo.fecha.strftime("%d.%m.%Y") if evo.fecha else "N/A",
                    evo.peso if evo.peso else "N/A",
                    evo.notas if evo.notas else "No hay notas."

                ))

            session_up_evo.close()

        except Exception as e:
            messagebox.showerror("Error",f"Error al actualizar: {e}")
    
    boton_agregar_evo = tb.Button(frame_botones_evo, text="Agregar Evolución", command = agregar_evolucion, bootstyle= "success")
    boton_agregar_evo.pack(side=LEFT,padx=5)


