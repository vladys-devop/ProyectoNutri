import ttkbootstrap as tb
from ttkbootstrap.constants import *
from views.login import login_view, crear_admin
from views.dashboard import vista_dashboard
from views.clientes import vista_clientes
from views.citas import vista_citas



def crear_interfaz():
    """
    Creamos la interzaf principal de la aplicación.
    Mostrará toda la información principal de la app. 
    """

    # CREAMOS USUARIO ADMIN POR DEFECTO

    crear_admin()


    # INICIAR LA VENTANA PRINCIPAL 

    app = tb.Window(themename="solar")
    app.title("Gestión de Clientes")
    app.geometry("1400x800")

    # MOSTRAR LOGIN

    login_aceptado = login_view(app)

    if not login_aceptado:
        app.destroy()
        return

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

    # MOSTRAR LA VISTA DEL DASHBOARD
    def ir_dashboard():
        mostrar_vista(vista_dashboard)


    # MOSTRAR LA VISTA DE CLIENTES
    def ir_clientes():
        mostrar_vista(vista_clientes)


    # MOSTRAR LA VISTA DE CITAS 
    def ir_citas():
        mostrar_vista(vista_citas)  

    # BOTONES SIDEBAR

    tb.Button(sidebar, text= "DASHBOARD",command = ir_dashboard,bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)
    tb.Button(sidebar, text= "CLIENTES", command= ir_clientes, bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)
    tb.Button(sidebar, text= "CITAS", command= ir_citas, bootstyle= "info",width= 25).pack(pady= 8, padx= 10, fill= X)



    app.mainloop()


if __name__ == "__main__":
    crear_interfaz()