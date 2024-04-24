import tkinter as tk
from tkinter import PhotoImage
from funciones import *

def cargar_imagen(ruta):
    return PhotoImage(file=ruta)

def crear_boton(root, imagen, command, relx, rely):
    boton = tk.Button(root, image=imagen, text="", compound="bottom", command=command)
    boton.place(relx=relx, rely=rely, anchor="center")
    return boton

# config ventana principal
ventana = tk.Tk()
ventana.title("Tinder??")
ventana.geometry("500x600")
ventana.configure(bg="green")

# config canvas blanco
canvas = tk.Canvas(ventana, bg="white", width=350, height=450)
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Cargar imgs
img_addUser = cargar_imagen("icons/agregar-usuario.png")
img_comunidad = cargar_imagen("icons/comunidad.png")
img_servicio = cargar_imagen("icons/mundo.png")
img_chat = cargar_imagen("icons/chat.png")
img_next = cargar_imagen("icons/flecha.png")
img_fyp = cargar_imagen("icons/fyp.png")
img_lupa = cargar_imagen("icons/lupa.png")
img_mail = cargar_imagen("icons/email.png")
img_usuario = cargar_imagen("icons/usuario.png")

# botones lado derecho
btn1 = crear_boton(ventana, img_addUser, funcBTN1, 0.93, 0.3)
btn2 = crear_boton(ventana, img_comunidad, funcBTN2, 0.93, 0.4)
btn3 = crear_boton(ventana, img_servicio, funcBTN3, 0.93, 0.5)
btn4 = crear_boton(ventana, img_chat, funcBTN4, 0.93, 0.6)

btn5 = crear_boton(ventana, img_next, lambda: funBTN5(canvas, "personas.json", etiqueta_nombre, etiqueta_edad, etiqueta_pronombre, etiqueta_descripcion), 0.93, 0.7)


# botones abajo
btn6 = crear_boton(ventana, img_fyp, funcBTN6, 0.25, 0.93)
btn7 = crear_boton(ventana, img_lupa, lambda: funBTN7("personas.json"), 0.4, 0.93)
btn8 = crear_boton(ventana, img_mail, funcBTN8, 0.6, 0.93)
btn9 = crear_boton(ventana, img_usuario, funcBTN9, 0.75, 0.93)


# ajustes parte blanco
ruta_imagen_perfil = "icons/avatarEjemplo.png"

mostrar_imagen(canvas, ruta_imagen_perfil)

# Etiqueta para nombre
etiqueta_nombre = tk.Label(canvas, text="Juan Pérez", font=("Arial", 12), bg="white")
etiqueta_nombre.place(relx=0.5, rely=0.4, anchor="center")

# Etiqueta para edad
etiqueta_edad = tk.Label(canvas, text="25 años", font=("Arial", 10), bg="white")
etiqueta_edad.place(relx=0.5, rely=0.45, anchor="center")

# Etiqueta para pronombre
etiqueta_pronombre = tk.Label(canvas, text="He", font=("Arial", 10), bg="white")
etiqueta_pronombre.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta para descrip
descripcion = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed aliquam ligula id neque mollis, eu porttitor magna fringilla. Nullam nec dui sit amet odio placerat vestibulum."
etiqueta_descripcion = tk.Label(canvas, text=descripcion, font=("Arial", 10), bg="white", wraplength=300, justify="center")
etiqueta_descripcion.place(relx=0.5, rely=0.6, anchor="center")

#usuario btn
img_Tw = PhotoImage(file="icons/nube.png")
btnTw = tk.Button(canvas, text="",image=img_Tw, compound="bottom", command=funcBTNTw)
btnTw.place(relx=0.5, rely=0.9, anchor="center")

# iniciar ventana
ventana.mainloop()
