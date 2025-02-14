import tkinter as tk
from tkinter import *

class VentanaInicio:

 def __init__(self):

# CONTADOR PARA IR MOSTRANDO LAS IMÁGENES DE LOS DESARROLLADORES
  self._contadorImgDll = 1
  
  # SALIR DEL PROGRAMA
  def eventoSalir():
    ventana.destroy()
  
  # DESCRIPCIÓN DE LA APP
  def eventoDescripcion():
    mensajeBienvenida.destroy()
    texto = tk.Text(P3,font=("Times",10))
    texto.insert(1.0,"Este es un sistema de redes reducido, con distintas generalidades abstraídas de la \nrealidad, mediante una aplicación implementada en Python que se basa en el paradigma \nde programación orientada a objetos. Cuenta con cinco funcionalidades que manejan \nplanes de contratación de servicio, cada plan le permite al usuario elegir entre una gama de características relacionadas con el servicio doméstico de Internet, entre otras \nacciones como cambio de plan.")
    texto.config(padx=15, pady=15, state="disabled")
    texto.place(x=0, y=0, height=144, width=500)
  
  # CAMBIO DE IMAGEN DE LOS DESARROLLADORES - Agregar las imagenes
  def cambioImg():
    self._contadorImgDll+=1
    if self._contadorImgDll==2:
      imagen1.config(file="")
      imagen2.config(file="")
      imagen3.config(file="")
      imagen4.config(file="")

      d1.config(textvariable=tk.StringVar(P5,value=" Valeria Moreno Rojas"))
      d3.config(textvariable=tk.StringVar(P5,value=" 18 años"))

    elif self._contadorImgDll==3:
      imagen1.config(file="")
      imagen2.config(file="")
      imagen3.config(file="")
      imagen4.config(file="")
      d1.config(textvariable=tk.StringVar(P5,value=" Justin Camilo Loaiza Lujan"))
      d3.config(textvariable=tk.StringVar(P5,value=" 18 años"))
    
    if self._contadorImgDll==4:
      imagen1.config(file="")
      imagen2.config(file="")
      imagen3.config(file="")
      imagen4.config(file="") 
      d1.config(textvariable=tk.StringVar(P5,value=" Maria Jose Monroy Mejia"))
      d3.config(textvariable=tk.StringVar(P5,value=" 19 años"))
      self._contadorImgDll=1

  ventana = tk.Tk()
  ventana.title("Ventana Inicio")
  ventana.geometry("900x500")
  ventana.resizable(0, 0)
  
#   FRAMES ANIDADOS
  P1 = tk.Frame(ventana, bg="black", height=500, width=500)
  P1.pack(side="left") 
  
  P2 = tk.Frame(ventana, bg="black", height=500, width=400)
  P2.pack(side="right")

  P3 = tk.Frame(P1, width=500, height=145)
  P3.place(x=5,y=5,width="500",height="145")

  P4 = tk.Frame(P1, width=500, height=338)
  P4.place(x=5,y=156,width="500",height="338")    
    
  P5 = tk.Frame(P2, width=390, height=145)
  P5.place(x=5,y=5,width="390",height="145")

  P6 = tk.Frame(P2, width=390, height=338)
  P6.place(x=5,y=156,width="390",height="338")

# BIENVENIDA
  mensajeBienvenida = tk.Label(P3, text="TE DAMOS LA BIENVENIDA A CONEXIA.\n\nEsperamos que tu experiencia sea agradable.\n\nHaz click en la parte inferior para ingresar a la ventana del usuario", font=("Times",9))
  mensajeBienvenida.place(x=45,y=35,width=400,height=75)

# IMÁGENES DEL SISTEMA
  contenedorImagenSis = tk.Label(P4)
  contenedorImagenSis.place(x=10, y=10, width="500", height="400")
  imagenSistema = tk.PhotoImage(file="") #imagen principal
  contenedorImagenSis.config(image=imagenSistema)

# BOTÓN PARA IR A LA VENTANA PRINCIPAL
  botonVentanaU = tk.Button(P4,text="Ir a la Ventana Principal")  ## comando ventana principal
  botonVentanaU.pack(side="bottom",anchor="c", pady=12)

 # CREAR MENU -> SALIR Y DESCRIPCION
  menuBar = tk.Menu(ventana)
  ventana.config(menu=menuBar)
  menu1 = tk.Menu(menuBar, tearoff = False)
  menuBar.add_cascade(label="Inicio",menu=menu1)
  menu1.add_command(label="Descripción", command=eventoDescripcion)
  menu1.add_command(label="Salir",command=eventoSalir)
         
# CONFIGURACIONES IMAGENES DESARROLLADORES - Imagenes de Majo
  imagen1 = tk.PhotoImage(file="")
  imagen2 = tk.PhotoImage(file="")
  imagen3 = tk.PhotoImage(file="")
  imagen4 = tk.PhotoImage(file="")
  pInterior = tk.Frame(P6, padx=25, pady=25)
  pInterior.pack(fill="both", expand=True)
  limg1=tk.Label(pInterior, image=imagen1, padx=10, pady=10)
  limg1.grid(row=0,column=0, sticky="nsew")
          
  limg2=tk.Label(pInterior,image=imagen2, padx=10, pady=10)
  limg2.grid(row=0,column=1,sticky="nsew")
          
  limg3=tk.Label(pInterior,image=imagen3, padx=10, pady=10)
  limg3.grid(row=1,column=0,sticky="nsew")
          
  limg4=tk.Label(pInterior,image=imagen4, padx=10, pady=10)
  limg4.grid(row=1,column=1,sticky="nsew") 
  
  # BOTÓN PARA CAMBIO IMAGENES DESARROLLADORES
  botonCambimg = tk.Button(P5, text="Desarrollador",command=cambioImg)
  botonCambimg.pack(side="bottom", anchor="c", pady=12)
  
  # DESCRIPCION DESARROLLADORES
  l1=tk.Label(P5,text="Nombre: ")
  l1.place(x=30, y=20)
  l2=tk.Label(P5,text="Programa: ")
  l2.place(x=30, y=50)
  l3=tk.Label(P5,text="Edad: ")
  l3.place(x=30, y=80)
  d1=tk.Entry(P5,state="disabled",textvariable=tk.StringVar(P5,value=" Maria Jose Monroy Mejia"))
  d1.place(x=100, y=20, height=20, width=200)
  d2=tk.Entry(P5,state="disabled",textvariable=tk.StringVar(P5,value=" Estadistica"))
  d2.place(x=100, y=50, height=20, width=200)
  d3=tk.Entry(P5,state="disabled",textvariable=tk.StringVar(P5,value=" 19 años"))
  d3.place(x=100, y=80, height=20, width=200)
  
  ventana.mainloop() 