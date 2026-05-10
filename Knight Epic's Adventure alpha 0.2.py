import tkinter as tk

def informacion():
    consejo = tk.Frame(lienzo)
    consejo.configure(width=1000, height=600, bg="lawn green", bd=1)
    consejo.pack()
    consejo.place(x=400, y=200)

    def retorno():
        consejo.destroy()
        regreso.destroy()
        acerca_de_1.destroy()
        acerca_de_2.destroy()
        acerca_de_3.destroy()
        creditos.destroy()
        creador.destroy()
    
    regreso = tk.Button(consejo, text="Volver a Inicio", command = retorno)
    regreso.configure(width=12, height=1, bg="purple1", bd=1 ,font=("Arial", 20))
    regreso.pack()
    regreso.place(x=100, y=50)

    acerca_de_1 = tk.Label(consejo, text="Eres un señor feudal que ha reclutado un grupo de 3 guerreros")
    acerca_de_1.configure(width=50, height=2, fg="gray8", bg="PaleGreen2", font=("times new roman", 24, "italic"))
    acerca_de_1.pack()
    acerca_de_1.place(x=100, y=150)

    acerca_de_2 = tk.Label(consejo, text="con el fin de combatir al grupo de otros feudales del continente")
    acerca_de_2.configure(width=50, height=2, fg="gray8", bg="PaleGreen2", font=("times new roman", 24, "italic"))
    acerca_de_2.pack()
    acerca_de_2.place(x=100, y=230)

    acerca_de_3 = tk.Label(consejo, text="por proteger tu castillo y enseñarles quien es el que manda")
    acerca_de_3.configure(width=50, height=2, fg="gray8", bg="PaleGreen2", font=("times new roman", 24, "italic"))
    acerca_de_3.pack()
    acerca_de_3.place(x=100, y=300)

    creditos = tk.Label(consejo, text="Creador:")
    creditos.configure(width=10, height=2, fg="gray8", bg="gold", font=("times new roman", 24, "italic"))
    creditos.pack()
    creditos.place(x=300, y=400)

    creador = tk.Label(consejo, text="The Gentle Ice")
    creador.configure(width=12, height=2, fg="gray8", bg="light goldenrod", font=("times new roman", 24, "italic"))
    creador.pack()
    creador.place(x=450, y=400)

def cambiar_seleccion_personaje():
    inicio.destroy()
    info.destroy()
    usuario.destroy()
    contexto.destroy()
    titulo.destroy()
    marco_titulo.destroy()
    entrada.destroy()
    castillo1.destroy()
    castillo2.destroy()
    castillo3.destroy()
    fondo1.destroy()

    fondo2 = tk.Frame(lienzo)
    fondo2.configure(width=1800, height=1000, bg="orange", bd=1)
    fondo2.pack()

    def cambiar_seleccion_compañeros():
        character3.destroy()
        character2.destroy()
        character1.destroy()
        avatar.destroy()
        select_ch.destroy()
        fondo2.destroy()

        fondo3 = tk.Frame(lienzo)
        fondo3.configure(width=1800, height=1000, bg="LemonChiffon4", bd=1)
        fondo3.pack()

        select_summons = tk.Frame(fondo3)
        select_summons.configure(width=1600, height=800, bg="bisque2", bd=1)
        select_summons.pack()
        select_summons.place(x=100, y=100)

        caballeros = tk.Label(select_summons, text="Selecciona tus guerreros")
        caballeros.configure(fg="red", bg="orange2", font=("Times New Roman", 52, "italic"))
        caballeros.pack()
        caballeros.place(x=475, y=50)

        summon1 = tk.Button(select_summons, text="Guerrero 1")
        summon1.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon1.pack()
        summon1.place(x=15, y=200)

        summon2 = tk.Button(select_summons, text="Guerrero 2")
        summon2.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon2.pack()
        summon2.place(x=330, y=200)

        summon3 = tk.Button(select_summons, text="Guerrero 3")
        summon3.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon3.pack()
        summon3.place(x=645, y=200)

        summon4 = tk.Button(select_summons, text="Guerrero 4")
        summon4.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon4.pack()
        summon4.place(x=960, y=200)

        summon5 = tk.Button(select_summons, text="Guerrero 5")
        summon5.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon5.pack()
        summon5.place(x=1270, y=200)

        summon6 = tk.Button(select_summons, text="Guerrero 6")
        summon6.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon6.pack()
        summon6.place(x=15, y=400)

        summon7 = tk.Button(select_summons, text="Guerrero 7")
        summon7.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon7.pack()
        summon7.place(x=330, y=400)

        summon8 = tk.Button(select_summons, text="Guerrero 8")
        summon8.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon8.pack()
        summon8.place(x=645, y=400)

        summon9 = tk.Button(select_summons, text="Guerrero 9")
        summon9.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon9.pack()
        summon9.place(x=960, y=400)

        summon10 = tk.Button(select_summons, text="Guerrero 10")
        summon10.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon10.pack()
        summon10.place(x=1270, y=400)

        summon11 = tk.Button(select_summons, text="Guerrero 11")
        summon11.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon11.pack()
        summon11.place(x=15, y=600)

        summon12 = tk.Button(select_summons, text="Guerrero 12")
        summon12.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon12.pack()
        summon12.place(x=330, y=600)

        summon13 = tk.Button(select_summons, text="Guerrero 13")
        summon13.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon13.pack()
        summon13.place(x=645, y=600)

        summon14 = tk.Button(select_summons, text="Guerrero 14")
        summon14.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon14.pack()
        summon14.place(x=960, y=600)

        summon15 = tk.Button(select_summons, text="Guerrero 15")
        summon15.configure(width=10, height=1, fg="gray8", bg="saddle brown", font=("times new roman", 40, "italic"))
        summon15.pack()
        summon15.place(x=1270, y=600)
    
    select_ch = tk.Frame(fondo2)
    select_ch.configure(width=1600, height=800, bg="medium sea green", bd=1)
    select_ch.pack()
    select_ch.place(x=100, y=100)

    avatar = tk.Label(select_ch, text="Selecciona tu personaje")
    avatar.configure(fg="DarkGoldenrod1", bg="firebrick4", font=("Times New Roman", 52, "italic"))
    avatar.pack()
    avatar.place(x=475, y=50)

    character1 = tk.Button(select_ch, text="Personaje 1", command = cambiar_seleccion_compañeros)
    character1.configure(width=12, height=7, fg="gray8", bg="gold2", font=("times new roman", 40, "italic"))
    character1.pack()
    character1.place(x=125, y=200)

    character2 = tk.Button(select_ch, text="Personaje 2", command = cambiar_seleccion_compañeros)
    character2.configure(width=12, height=7, fg="gray8", bg="gold2", font=("times new roman", 40, "italic"))
    character2.pack()
    character2.place(x=625, y=200)

    character3 = tk.Button(select_ch, text="Personaje 3", command = cambiar_seleccion_compañeros)
    character3.configure(width=12, height=7, fg="gray8", bg="gold2", font=("times new roman", 40, "italic"))
    character3.pack()
    character3.place(x=1125, y=200)
    
lienzo = tk.Tk()
lienzo.title("Knight Epic's Adventure")
lienzo.geometry("1800x1000+50+10")
lienzo.resizable(False, False)

fondo1 = tk.Frame(lienzo)
fondo1.configure(width=1800, height=1000, bg="cyan2", bd=1)
fondo1.pack()

castillo1 = tk.Frame(lienzo)
castillo1.configure(width=500, height=800, bg="wheat2", bd=1)
castillo1.pack()
castillo1.place(x=0,y=200)

castillo2 = tk.Frame(lienzo)
castillo2.configure(width=500, height=800, bg="wheat2", bd=1)
castillo2.pack()
castillo2.place(x=1300,y=200)

castillo3 = tk.Frame(lienzo)
castillo3.configure(width=800, height=600, bg="wheat3", bd=1)
castillo3.pack()
castillo3.place(x=500,y=400)

entrada = tk.Frame(lienzo)
entrada.configure(width=300, height=400, bg="gray1", bd=1)
entrada.pack()
entrada.place(x=775,y=600)

marco_titulo = tk.Frame(lienzo)
marco_titulo.configure(width=800, height=150, bg="firebrick4", bd=1)
marco_titulo.pack()
marco_titulo.place(x=500, y=100)

titulo = tk.Label(marco_titulo, text="Knight Epic's Adventure")
titulo.configure(fg="DarkGoldenrod1", bg="firebrick4", font=("Times New Roman", 52, "italic"))
titulo.pack()
titulo.place(x=50, y=30)

info = tk.Button(lienzo, text="About", command = informacion)
info.configure(width=10, height=2, bg="magenta2", bd=1 ,font=("Arial", 20))
info.pack()
info.place(x=150, y=50)

usuario = tk.Entry(lienzo)
usuario.configure(width=15, bg="azure2", font=("Arial", 24))
usuario.pack()
usuario.place(x=865, y=350)

contexto = tk.Label(lienzo, text="Nombre de Usuario:")
contexto.configure(fg="DarkGoldenrod1", bg="firebrick3", font=("Times New Roman", 24))
contexto.pack()
contexto.place(x=600, y=350)

inicio = tk.Button(lienzo, text="Iniciar Nueva Partida", command = cambiar_seleccion_personaje)
inicio.configure(width=20, height=2, bg="magenta2", bd=1 ,font=("Arial", 20))
inicio.pack()
inicio.place(x=750, y=450)
