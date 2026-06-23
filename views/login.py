import ttkbootstrap as tb
from ttkbootstrap.constants import *
from database.database import Session, Usuario
import bcrypt
from datetime import datetime

"""
Módulo de autenticación y login de la aplicación.
Gestion de la creación del usuario Admin y Login de la app.
"""


def crear_admin():
    """
    Crea el usuario Admin por defecto..
    
    Credenciales por defecto:

    Usuario: admin
    Contraseña: admin
    """
    try:
        session = Session()
        admin = session.query(Usuario).filter_by(nombre_usuario="admin").first()

        if not admin:
            # GENERAMOS EL HASHEADO DE LA CONTRASEÑA
            pass_hash = bcrypt.hashpw("admin".encode(), bcrypt.gensalt()).decode()
            
            # CREAMOS UN NUEVO USUARIO ADMIN 
            nuevo_usuario = Usuario(
                nombre_usuario="admin",
                password=pass_hash,
                email="admin@nutri.com",
                fecha_creacion=datetime.now()
            )

            session.add(nuevo_usuario)
            session.commit()

        session.close()
    except Exception as e:
        print(f"Error al crear admin: {e}")

# CREAMOS LA PANTALLA DE LOGIN
def login_view(parent):
    
    login_exitoso = [False]  # GUARDAMOS EL ESTADO DEL LOGIN EN UNA VARIABLE

    # CREAR VENTANA DE LOGIN
    ventana_login = tb.Toplevel(parent)
    ventana_login.title("Login - Gestión de Clientes")
    ventana_login.geometry("400x400")
    ventana_login.resizable(False, False)

    # CENTRAMOS LA VENTANA DE LOGIN EN LA PANTALLA PRINCIPAL
    ventana_login.update_idletasks()
    ancho_login = ventana_login.winfo_width()
    alto_login = ventana_login.winfo_height()
    
    x_parent = parent.winfo_x()
    y_parent = parent.winfo_y()
    ancho_parent = parent.winfo_width()
    alto_parent = parent.winfo_height()
    
    # FÓRMULA PARA CALCULAR LA POSICIÓN CENTRADA
    x = x_parent + (ancho_parent // 2) - (ancho_login // 2)
    y = y_parent + (alto_parent // 2) - (alto_login // 2)
    
    ventana_login.geometry(f"{ancho_login}x{alto_login}+{x}+{y}")

    # HACEMOS UNA VENTANA MODAL
    """
    Lo que permite la ventana modal es que no puedas clickear sobre la otra
    mientras la ventana de Login este abierta. 
    """
    ventana_login.grab_set()
    ventana_login.transient(parent)

    # TÍTULO
    tb.Label(ventana_login, text="Login", font=("Arial", 18, "bold")).pack(pady=30)

    # CAMPO USUARIO
    tb.Label(ventana_login, text="Usuario:").pack(pady=5, padx=20, anchor=W)
    entry_usuario = tb.Entry(ventana_login, width=30)
    entry_usuario.pack(pady=5, padx=20, fill=X)
    entry_usuario.focus()  

    # CAMPO CONTRASEÑA
    tb.Label(ventana_login, text="Contraseña:").pack(pady=5, padx=20, anchor=W)
    entry_password = tb.Entry(ventana_login, width=30, show="*")
    entry_password.pack(pady=5, padx=20, fill=X)

    # LABEL PARA MENSAJES DE ERROR
    label_error = tb.Label(ventana_login, text="", foreground="red")
    label_error.pack(pady=10)

    # VALIDACIÓN DEL LOGIN

    def validar_login():
        # VALIDAMOS SI LAS CREDENCIALES SON CORRECTAS

        usuario = entry_usuario.get().strip()
        password = entry_password.get()

        # VALIDAR CAMPOS NO VACIOS 
        if not usuario or not password:
            label_error.config(text="Usuario y contraseña requeridos")
            return

        try:
            session = Session()
            user = session.query(Usuario).filter_by(nombre_usuario=usuario).first()
            session.close()

        
            if user and bcrypt.checkpw(password.encode(), user.password.encode()):
                login_exitoso[0] = True 
                ventana_login.destroy()  
            else:
                label_error.config(text="Usuario o contraseña incorrectos")
                entry_password.delete(0, END) 
                entry_usuario.focus()  

        except Exception as e:
            label_error.config(text=f"Error: {e}")
            print(f"Error en login: {e}")

    # BOTÓN DE LOGIN

    boton_login = tb.Button(ventana_login,text="Iniciar Sesión",command=validar_login,bootstyle="success")
    boton_login.pack(pady=20)

    # PARA PODER PERMITIR USAR LA TECLA ENTER EN EL LOGIN
    entry_password.bind("<Return>", lambda e: validar_login())

    # ESPERAR A QUE SE CIERRE LA VENTANA
    ventana_login.wait_window()

    return login_exitoso[0]  # DEVOLVEMOS SI EL LOGIN FUE EXITOSO