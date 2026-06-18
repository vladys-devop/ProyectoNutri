import ttkbootstrap as tb
from ttkbootstrap.constants import *
from database.database import Session, Usuario
import bcrypt
from datetime import datetime

def crear_admin():
    session = Session()
    admin = session.query(Usuario).filter_by(nombre_usuario = "admin").first()

    if not admin: 
        pass_hash = bcrypt.hashpw("admin".encode(), bcrypt.gensalt()).decode()
        nuevo_usuario = Usuario(
            nombre_usuario ="admin",
            password = pass_hash,
            email = "admin@nutri.com",
            fecha_creacion = datetime.now()
        )

        session.add(nuevo_usuario)
        session.commit()

    session.close()

def login_view(parent):

    ventana_login = tb.Toplevel(parent)
    ventana_login.title("Login")
    ventana_login.geometry("400x400")
    ventana_login.resizable(False,False)


    # CENTRAR VENTANA

    ventana_login.update_idletasks()
    ancho_login = ventana_login.winfo_width()
    alto_login = ventana_login.winfo_height()
    
    x_parent = parent.winfo_x()
    y_parent = parent.winfo_y()
    ancho_parent = parent.winfo_width()
    alto_parent = parent.winfo_height()
    
    x = x_parent + (ancho_parent // 2) - (ancho_login // 2)
    y = y_parent + (alto_parent // 2) - (alto_login // 2)
    
    ventana_login.geometry(f"{ancho_login}x{alto_login}+{x}+{y}")

    ventana_login.grab_set()
    ventana_login.transient(parent)

    # TÍTULO 

    titulo = tb.Label(ventana_login, text="Login", font=("Arial", 18, "bold")).pack(pady=30)


    # USUARIO 

    tb.Label(ventana_login, text="Usuario:").pack(pady=5, padx=20, anchor=W)
    entry_usuario = tb.Entry(ventana_login,width=30)
    entry_usuario.pack(pady=5,padx=20,fill=X)

    # CONTRASEÑA 

    tb.Label(ventana_login,text="Contraseña:").pack(pady=5,padx=20,anchor=W)
    entry_password = tb.Entry(ventana_login,width=30, show="*")
    entry_password.pack(pady=5,padx=20,fill=X)

    # LABEL MENSAJES

    label_error = tb.Label(ventana_login,text="",foreground="red")
    label_error.pack(pady=10)

    def validar_login():
        usuario = entry_usuario.get()
        password = entry_password.get()

        if not usuario or  not password: 
            label_error.config(text="Usuario o contraseña requeridos")
            return
        
        session = Session()
        user = session.query(Usuario).filter_by(nombre_usuario = usuario).first()
        session.close()

        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            ventana_login.destroy()
            return True
        else: 
            label_error.config(text="Usuario o contraseña incorrectos")
            entry_password.delete(0,END)

    # BOTÓN LOGIN 

    boton_login = tb.Button(ventana_login, text="Iniciar Sesión", command= validar_login,bootstyle="success")
    boton_login.pack(pady=20)

    ventana_login.wait_window()
    