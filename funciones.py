import tkinter as tk
from tkinter import PhotoImage
import json

def funcBTN1():
    # Crear una nueva ventana emergente
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Persona Añadida")
    ventana_emergente.geometry("200x100")
    
    # Etiqueta con el mensaje
    etiqueta_mensaje = tk.Label(ventana_emergente, text="¡Persona Añadida!", font=("Arial", 12))
    etiqueta_mensaje.pack(pady=20)
    
    # Funcion para cerrar la ventana emergente
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    # Btn de aceptar
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    # Hacer que no se cierre
    ventana_emergente.grab_set()

def funcBTN2():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Comunidad")
    ventana_emergente.geometry("200x220")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="¡Persona Añadida a la Comunidad!", font=("Arial", 12),wraplength=100)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()

def funcBTN3():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Servicio Comunitario")
    ventana_emergente.geometry("200x230")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="¡Comunicate con el candidato para el Servicio Comunitario!", font=("Arial", 12),wraplength=100)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()

def funcBTN4():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Chatear")
    ventana_emergente.geometry("200x150")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="¡Inicia una conversación!", font=("Arial", 12),wraplength=100)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()

def funcBTN6():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Interactuar")
    ventana_emergente.geometry("300x200")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="Aquí es donde puede interactuar con los otros perfiles o ver a los perfiles que usted sigue y le interesan", font=("Arial", 12),wraplength=200)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()

def funcBTN8():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Mensajes")
    ventana_emergente.geometry("300x200")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="Bandeja de entrada. Se encuentran los chats con las personas seleccionadas o los “match”", font=("Arial", 12),wraplength=200)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()

def funcBTN9():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Perfil")
    ventana_emergente.geometry("200x230")
    
    etiqueta_mensaje = tk.Label(ventana_emergente, text="Organiza tu perfil.", font=("Arial", 12),wraplength=100)
    etiqueta_mensaje.pack(pady=20)
    
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    ventana_emergente.grab_set()


def cargarJson(ruta_json):
    with open(ruta_json, 'r') as file:
        datos = json.load(file)
    return datos

def crear_imagen_redonda(canvas, ruta, x, y, radio):
    imagen = tk.PhotoImage(file=ruta)
    image = canvas.create_image(x, y, image=imagen, anchor="center")
    #canvas.create_oval(x - radio, y - radio, x + radio, y + radio, outline="white", width=3)
    canvas.imagen = image
    print("hola", canvas.imagen)
    return imagen

def mostrar_imagen(canvas, ruta_imagen):
    # Cargar la imagen usando PhotoImage de tkinter
    imagen_tk = tk.PhotoImage(file=ruta_imagen)
    
    # Crear un Label y mostrar la imagen
    label_imagen = tk.Label(canvas, image=imagen_tk)
    label_imagen.image = imagen_tk  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
    label_imagen.place(relx=0.5, rely=0.2, anchor="center")

indice_actual = 0
def funBTN5(canvas, ruta_json, etiqueta_nombre, etiqueta_edad, etiqueta_pronombre, etiqueta_descripcion):
    global indice_actual

    # Cargar los datos desde el JSON
    datos = cargarJson(ruta_json)
    
    # Verificar si el índice actual está dentro del rango de datos
    if 0 <= indice_actual < len(datos):
        persona = datos[indice_actual]
        nombre_apellido = persona.get("nombreApellido", "")
        edad = persona.get("edad", "")
        pronombre = persona.get("pronombre", "")
        descripcion = persona.get("descripcion", "")
        imagen_perfil = persona.get("imagen_perfil", "")

        # Actualizar las etiquetas en el canvas
        etiqueta_nombre.config(text=nombre_apellido)
        etiqueta_edad.config(text=f"{edad} años")
        etiqueta_pronombre.config(text=pronombre)
        etiqueta_descripcion.config(text=descripcion)
        
        # Cargar la imagen de perfil desde el archivo correspondiente
        ruta_imagen = f"perfiles/{imagen_perfil}.png" 
        mostrar_imagen(canvas, ruta_imagen)
        
        # Incrementar el índice actual para la próxima vez
        indice_actual += 1
        # Reiniciar el índice al principio si llega al final de la lista
        if indice_actual >= len(datos):
            indice_actual = 0
    else:
        print(f"Índice inválido: {indice_actual}")

def buscar_perfil(ruta_json, termino_busqueda):
    try:
        with open(ruta_json, "r") as file:
            data = json.load(file)
            
            # Buscar el perfil que coincida con el término de búsqueda
            for perfil in data:
                nombre_apellido = perfil.get("nombreApellido", "")
                if termino_busqueda.lower() in nombre_apellido.lower():
                    return perfil
            
            # Si no se encuentra ningún perfil, retornar None
            return None
    except FileNotFoundError:
        messagebox.showerror("Error", f"Archivo JSON no encontrado: {ruta_json}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al buscar perfil: {e}")
        return None

def funBTN7(ruta_json):
    def buscar():
        termino_busqueda = entry_busqueda.get().strip()
        
        if termino_busqueda:
            perfil_encontrado = buscar_perfil(ruta_json, termino_busqueda)
            if perfil_encontrado:
                # Mostrar información del perfil encontrado en la ventana emergente
                ventana_resultado = tk.Toplevel()
                ventana_resultado.title("Resultado de Búsqueda")
                
                tk.Label(ventana_resultado, text=f"Nombre: {perfil_encontrado.get('nombreApellido', '')}").pack()
                tk.Label(ventana_resultado, text=f"Edad: {perfil_encontrado.get('edad', '')} años").pack()
                tk.Label(ventana_resultado, text=f"Sexo: {perfil_encontrado.get('pronombre', '')}").pack()
                tk.Label(ventana_resultado, text=f"Descripción: {perfil_encontrado.get('descripcion', '')}").pack()
            else:
                ventana_resultado = tk.Toplevel()
                ventana_resultado.title("Resultado de Búsqueda")
                
                tk.Label(ventana_resultado, text=f"No se encontró ningún perfil con el término '{termino_busqueda}'").pack()
        else:
            print("Búsqueda", "Ingrese un término de búsqueda válido")

    # Crear la ventana emergente para buscar perfil
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Buscar Perfil")

    tk.Label(ventana_emergente, text="Buscar Perfil por Nombre:").pack()
    entry_busqueda = tk.Entry(ventana_emergente, width=30)
    entry_busqueda.pack(pady=10)
    
    btn_buscar = tk.Button(ventana_emergente, text="Buscar", command=buscar)
    btn_buscar.pack()

def funcBTNTw():
    # Crear una nueva ventana emergente
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Comunidad")
    ventana_emergente.geometry("200x220")
    
    # Etiqueta con el mensaje
    etiqueta_mensaje = tk.Label(ventana_emergente, text="Ten acceso a los Tweets y mas informacion", font=("Arial", 12),wraplength=100)
    etiqueta_mensaje.pack(pady=20)
    
    # Función para cerrar la ventana emergente
    def cerrar_ventana():
        ventana_emergente.destroy()
    
    # Botón de aceptar para cerrar la ventana emergente
    btn_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=cerrar_ventana)
    btn_aceptar.pack()

    # Hacer que la ventana emergente permanezca arriba
    ventana_emergente.grab_set()