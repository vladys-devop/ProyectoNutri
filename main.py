import ttkbootstrap as tb
from ttkbootstrap.constants import *
from views.login import login_view, crear_admin
from views.dashboard import vista_dashboard
from views.clientes import vista_clientes
from views.citas import vista_citas

# CREAMOS 1 ADMIN

crear_admin()


app = tb.Window(themename="solar")

app.title("Gestió Clients")
app.geometry("1400x800")

# MOSTRAR LOGIN

login_view(app)




# MENÚ LATERAL 

sidebar = tb.Frame(app, bootstyle="dark")
sidebar.pack(side= LEFT, fill= BOTH)
sidebar.config(width= 200)
sidebar.pack_propagate(False)

# CONTENIDO (LADO DERECHO)

contenedor = tb.Frame(app)
contenedor.pack(side= RIGHT, fill= BOTH, expand= True, padx= 10, pady= 10)

# TÍTULO SIDEBAR

titulo = tb.Label(sidebar, text= "MENÚ", font=("Arial", 14, "bold"), bootstyle= "light")
titulo.pack(pady= 15, padx= 10)



def mostrar_vista(vista_function):
    # LIMPIAR CONTENEDOR
    for widget in contenedor.winfo_children():
        widget.destroy()

    vista_function(contenedor)

def ir_dashboard():
    mostrar_vista(vista_dashboard)

def ir_clientes():
    mostrar_vista(vista_clientes)

def ir_citas():
    mostrar_vista(vista_citas)  

# BOTONES SIDEBAR

tb.Button(sidebar, text= "DASHBOARD",command = ir_dashboard,bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)
tb.Button(sidebar, text= "CLIENTES", command= ir_clientes, bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)
tb.Button(sidebar, text= "CITAS", command= ir_citas, bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)



app.mainloop()