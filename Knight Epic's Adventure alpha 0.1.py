import tkinter as tk

fondo = tk.Tk()
fondo.title("Knight Epic's Adventure")
fondo.geometry("1800x1000+50+10")
fondo.configure(bg="cyan2")
fondo.resizable(False, False)

castillo1 = tk.Frame(fondo)
castillo1.configure(width=500, height=800, bg="wheat2", bd=1)
castillo1.pack()
castillo1.place(x=0,y=200)

castillo2 = tk.Frame(fondo)
castillo2.configure(width=500, height=800, bg="wheat2", bd=1)
castillo2.pack()
castillo2.place(x=1300,y=200)

castillo3 = tk.Frame(fondo)
castillo3.configure(width=800, height=600, bg="wheat3", bd=1)
castillo3.pack()
castillo3.place(x=500,y=400)

entrada = tk.Frame(fondo)
entrada.configure(width=300, height=400, bg="gray1", bd=1)
entrada.pack()
entrada.place(x=775,y=600)

marco_titulo = tk.Frame(fondo)
marco_titulo.configure(width=800, height=150, bg="firebrick4", bd=1)
marco_titulo.pack()
marco_titulo.place(x=500, y=100)

titulo = tk.Label(marco_titulo, text="Knight Epic's Adventure")
titulo.configure(fg="DarkGoldenrod1", bg="firebrick4", font=("Times New Roman", 52, "italic"))
titulo.pack()
titulo.place(x=50, y=30)

info = tk.Button(fondo, text="About")
info.configure(width=10, height=2, bg="magenta2", bd=1 ,font=("Arial", 20))
info.pack()
info.place(x=150, y=50)

usuario = tk.Entry(fondo)
usuario.configure(width=20, font=("Arial", 24))
usuario.pack()
usuario.place(x=850, y=350)

contexto = tk.Label(fondo, text="Nombre de Usuario:")
contexto.configure(fg="DarkGoldenrod1", bg="firebrick3", font=("Times New Roman", 24))
contexto.pack()
contexto.place(x=600, y=350)

inicio = tk.Button(fondo, text="Iniciar Nueva Partida")
inicio.configure(width=20, height=2, bg="magenta2", bd=1 ,font=("Arial", 20))
inicio.pack()
inicio.place(x=750, y=450)
