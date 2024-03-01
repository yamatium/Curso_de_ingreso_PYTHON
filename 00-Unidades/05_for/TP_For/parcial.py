import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

Porcentaje de dinero en función de cada juego

"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        


    def btn_comenzar_ingreso_on_click(self):

        seguir = True
        maximo = 0
        dinero_ganado_ruleta = 0
        Jugadores_ruleta = 0

        jugadores_tragamonedas = 0
        jugadores = 0

        contador_Ruleta = 0
        contador_Poker  = 0
        contador_tragamonedas = 0
        
        while seguir == True:
            #ingreso de datos y validaciones
              
            nombre = prompt("Nombre", "Ingrese el nombre")
            importeGanado = int(prompt("importe", "ingrese el importe"))
            while importeGanado <= 1000:
                importeGanado   = prompt("Error", "Reingrese el importe")  
                importeGanado   = int(importeGanado)

                

            genero = prompt("Genero","Ingrese genero: Masculino - Femenino - Otro")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error","Reingrese genero: Masculino - Femenino - Otro")   
           
            juego = prompt("Juego","Ingrese juego: Ruleta, Poker, Tragamonedas")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("Error","Reingrese Juego: Ruleta, Poker, Tragamonedas")
                

            match juego:
                case "Ruleta":
                    contador_Ruleta +=1
                    Jugadores_ruleta +=1
                    dinero_ganado_ruleta += importeGanado
                    
                case "Tragamonedas":
                    contador_tragamonedas +=1
                    jugadores_tragamonedas +=1
                
                case _:
                    contador_Poker +=1
                    pass
                    
            
            
            if importeGanado > maximo:
                    maximo = importeGanado
                    nombre_maximo_importe = nombre
                    genero_maximo_importe = genero

            seguir = question("Seguir", "Desea continuar?")

        if jugadores > 0:
            jugadores +=1

        if Jugadores_ruleta > 0:
            promedio_dinero_ganado_ruleta = dinero_ganado_ruleta / Jugadores_ruleta 
            print(f"2.el promedio de dinero ganado en ruleta fue de {promedio_dinero_ganado_ruleta}$") 
        if jugadores_tragamonedas > 0:
            porcentaje_jugadores_tragamonedas = jugadores * 100 / jugadores_tragamonedas
            print(f"3. el porcentaje de personas que jugaron en el tragamonedas fue de {porcentaje_jugadores_tragamonedas} ")

        if   contador_Ruleta < contador_Poker and contador_Ruleta < contador_tragamonedas:
            print("4.Ruleta fue el juego menos elegido")
        elif contador_Poker < contador_Ruleta and contador_Poker < contador_tragamonedas:
            print("4.Poker fue el juego menos elegido")
        else:
            print("4.Tragamonedas fue el menos elegido")

       
        
        print(f"1. {nombre_maximo_importe} del genero {genero_maximo_importe} ha sido el que mas gano con {maximo}$")
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
