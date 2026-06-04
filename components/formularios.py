import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from database.database import Session, Cliente
from datetime import datetime

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

