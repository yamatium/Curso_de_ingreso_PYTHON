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

1. Nombre y género de la persona que más ganó.
2. Promedio de dinero ganado en Ruleta.
3. Porcentaje de personas que jugaron en el Tragamonedas.
4. Cuál es el juego menos elegido por los ganadores.
5. Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
6. Porcentaje de dinero en función de cada juego

7. Nombre del jugador que mas dinero gano jugando poker

"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        


    def btn_comenzar_ingreso_on_click(self):

        importe_maximo = 0
        bandera_maximo = True

        acumulador_importe_ruleta = 0
        acumulador_importe_poker = 0
        acumulador_importe_tragamonedas = 0

        jugadores_ruleta = 0
        jugadores_poker = 0
        jugadores_tragamonedas = 0
        jugadores_no_poker = 0
        acumulador_importe_no_poker = 0
        
        seguir = True
        while seguir:
            #entrada de datos
            nombre = input("Ingrese su nombre:")
            importe_ganado = input("Ingrese importe:")
            importe_ganado = float(importe_ganado)
            

            while importe_ganado < 1000:
                importe_ganado = input("Reingrese importe: ")
                importe_ganado = float(importe_ganado)
            
            genero = input("Ingrese su genero: ")
            while genero != "Masculino" and genero != "Femenino" and genero !="Otro":
                genero = input("Reingrese su genero:")

            juego = input("Ingrese juego: ")
            while juego != "Ruleta" and juego != "Poker" and juego !="Tragamonedas":
                juego = input("Reingrese el juego:")

            match juego:
                case "Ruleta":
                    acumulador_importe_ruleta += importe_ganado
                    jugadores_ruleta  += 1
                case "Poker":
                    acumulador_importe_poker += importe_ganado
                    jugadores_poker +=1
                case "Tragamonedas":
                    acumulador_importe_tragamonedas += importe_ganado
                    jugadores_tragamonedas +=1

            #1. Nombre y género de la persona que más ganó:
            if importe_ganado > importe_maximo or bandera_maximo == True:
                importe_maximo = importe_ganado
                nombre_maximo  = nombre
                genero_maximo  = genero
                bandera_maximo = False


            if juego !="Poker" and importe_ganado > 15000:
                jugadores_no_poker +=1
                acumulador_importe_no_poker += importe_ganado

            seguir=question("Ingresa otro?", "desea ingresar otra entrada?")

            #2. Promedio de dinero ganado en Ruleta.
            if jugadores_ruleta > 0:
                promedio_dinero_ruleta = acumulador_importe_ruleta / jugadores_ruleta
            else:
                promedio_dinero_ruleta = "nadie jugo a la ruleta"

            #3. Porcentaje de personas que jugaron en el Tragamonedas.
            cantidad_ganadores = jugadores_ruleta + jugadores_poker + jugadores_tragamonedas
            porcentaje_tragamonedas = (jugadores_tragamonedas * 100) / cantidad_ganadores

            #4.Cuál es el juego menos elegido por los ganadores.
            if jugadores_ruleta < jugadores_poker and jugadores_ruleta < jugadores_tragamonedas:
                menos_jugado = "ruleta"
            elif jugadores_poker < jugadores_tragamonedas:
                menos_jugado = "poker"
            else :
                menos_jugado = "tragamonedas"

            
            #5. Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
            if jugadores_no_poker > 0:
                promedio_no_poker = acumulador_importe_no_poker / jugadores_no_poker
            else:
                promedio_no_poker = "todos jugaron poker"

            #6
            total_acumulado = acumulador_importe_poker + acumulador_importe_tragamonedas + acumulador_importe_ruleta

            porcentaje_total_poker = (acumulador_importe_poker * 100) / total_acumulado
            porcentaje_total_tragamonedas = (acumulador_importe_tragamonedas * 100) / total_acumulado
            porcentaje_total_ruleta = (acumulador_importe_ruleta * 100) / total_acumulado

            print(f"1. Nombre y género de la persona que más ganó: {nombre_maximo}, del genero: {genero_maximo} gano mas con: {importe_maximo}$ ")
            print(f"2. Promedio de dinero ganado en Ruleta. {promedio_dinero_ruleta}")
            print(f"3. Porcentaje de personas que jugaron en el Tragamonedas. {porcentaje_tragamonedas} %")
            print(f"4. Cuál es el juego menos elegido por los ganadores.  fue el {menos_jugado}")
            print(f"5. Promedio de importe ganado de las personas que NO jugaron Poker cuando el importe supere los $15000 {promedio_no_poker}")
            print(f"6. Porcentaje de dinero en función de cada juego {porcentaje_total_poker} {porcentaje_total_tragamonedas} {porcentaje_total_ruleta}")

        
  
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()