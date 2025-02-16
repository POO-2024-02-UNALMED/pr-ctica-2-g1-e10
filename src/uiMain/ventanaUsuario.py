import tkinter as tk
from tkinter import  messagebox
from fieldFrame import FieldFrame
from proveedorInternet import ProveedorInternet
from servidor import Servidor
from cliente import Cliente
from router import Router
from dispositivo import Dispositivo
from antena import Antena
from serializador import Serializador
from mes import Mes

class VentanaUsuario:

   _abierto = False
   frame_display=None
   proveedor_cliente=None
   cliente_=None
   titulo=None
   descripcion=None

   def __init__(self):

      def programa():
         for widget in ventana.winfo_children():
            widget.destroy()
       # PARA VOLVER A LA VENTANA DE INICIO
         def eventoSalir():

            from ventanaInicio import VentanaInicio

            ventana.destroy()
            VentanaUsuario._abierto = False
            Serializador.serializar()
            ventanaInicio = VentanaInicio()

         # REGRESO A LA PAGINA INICIAL PARA LA FUNCIONALIDAD TEST
         def eventoUsuario():
            self.frame_display.destroy()
            self.titulo.config(text="BIENVENIDO A LA VENTANA PRINCIPAL", font=("Times", 12), bg="gray85")
            self.descripcion.config( 
            text=" A continuación te daremos las instrucciones sobre cómo utilizar la aplicación:\n\n1. En la parte superior de esta ventana encontrarás un menú con tres pestañas: Archivo, Procesos y Consultas, Ayuda.\n\n2. En Archivo se desplegarán dos opciones:\n\n\t2.1. Aplicación, te dará información sobre el programa.\n\t2.2. Salir, sirve para regresar a la ventana de inicio. \n\n3. En Procesos y Consultas se listarán cada una de las funcionalidades. Da click en la opción que desees. \n\n4. Finalmente, en Ayuda tendrás la opción de Acerca de, esto te dará información sobre los autores del programa.", font=("Times",12), bg="gray85", justify="left")
            frameInformacion = tk.Frame(mainFrame, bg="gray85", height=270, width=670) #gray82
            frameInformacion.pack(expand=True, fill="both", padx=5, pady=5)
            
         # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
         # PARA ABRIR LA VENTANA DE DIÁLOGO CON LA INFO DE LA APP
         def eventoAplicacion():
            messagebox.showinfo(title = "Información de la Aplicación", message = "SISTEMA DE REDES",
            detail = "La aplicacion permite adquirir un plan de Internet con una compañía determinada y realizar cambios en el mismo, así como algunas funciones de administrador.")

         # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
         # PARA ABRIR LA VENTANA DE DIALOGO CON LA INFORMACION DE LOS AUTORES
         def eventoAcercaDe():
            messagebox.showinfo(title = "Información Autores", message = "AUTORES:",
            detail = "Angelica María Arce Parra \nLuisa María Marin Ceferino \nYesica Andrea Henao Ceballos \nJuan Camilo Misas Tabares \nFreddy Quintero Colorado")
         
         # RETORNO AL LA PANTALLA DE INICIO AL FINAL DE CADA FUNCIONALIDA
         def finalizar(): 
            programa()






            # //////////////////////////////////////////////////////////////////////////////////////////////////////
            # SE ELIMINAN LOS FRAMES YA CREADOS----PARA CAMBIAR ENTRE FUNCIONALIDADES
            for widget in frameInformacion.winfo_children():
               widget.destroy()


            # SE AJUSTA EL TITULO Y DESCRIPCION DE LA FUNCIONALIDAD
            self.titulo.config(text="ADQUISICIÓN DE UN PLAN", font=("Times",20))
            self.descripcion.config(wraplength=500, text="Esta funcionalidad tiene por objetivo que un usuario nuevo pueda registrarse en el sistema y a su vez compre un plan con las características específicas que brinda el proveedor de su preferencia.")

            # SE CONSTRUYE EL FIELDFRAME QUE SOLICITA LOS DATOS CORRESPONDIENTES
            criterios = ["Tipo de Usuario", "Nombre", "Documento", "Sede"]
            fp =FieldFrame(frameInformacion, "Datos solicitados", criterios, "Valor", ["Cliente", "", "", ""])
            fp.configure(borderwidth=1, relief="raised")
            fp.pack(fill="y",pady=10, padx=5)

            # SE AJUSTAN LOS BOTONES DE ACEPTAR Y BORRAR
            frameInterior = tk.Frame(frameInformacion, bg="gray84", height=100, width=300)
            frameInterior.pack( expand=True, fill="none", padx=100, pady=20,anchor="n")
            aceptar_button = tk.Button(frameInterior, text="Aceptar", command=eventoAceptar)
            borrar_button = tk.Button( frameInterior, text="Borrar", command=fp.borrarValores)
            aceptar_button.pack( side="left", pady=20, padx=50, anchor="sw")
            borrar_button.pack( side="left", pady=20, padx=40, anchor="se")