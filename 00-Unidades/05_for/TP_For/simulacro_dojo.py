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

        seguir = True
        importe_maximo = 0
        bandera_maximo = True
        contador_ruleta = 0
        acumulador_importe_ruleta = 0
        contador_tragamonedas = 0
        contador_poker = 0
        contador_no_poker = 0
        acumulador_importe_no_poker = 0
        acumulador_importe_poker = 0
        acumulador_importe_tragamonedas = 0
        importe_maximo_poker = 0
        nombre_maximo_poker = None

        
        while seguir:
            #entradas
            nombre = input("Ingrese nombre: ")

            importe_ganado = input("Ingrese importe: ")
            importe_ganado = float(importe_ganado)
            while importe_ganado < 1000:
                 importe_ganado = input("Reingrese importe: ")
                 importe_ganado = float(importe_ganado)
        
            genero = input("Ingrese genero: ")
            while genero != "Masculino" and genero!= "Femenino" and genero != "Otro":
                genero = input("Reingrese genero: ")

            juego = input("Ingrese juego: ")
            while juego != "Ruleta" and genero!= "Poker" and genero != "Tragamonedas":
                juego = input("Reingrese juego: ")

            if importe_ganado > importe_maximo or bandera_maximo == True:
                importe_maximo = importe_ganado
                nombre_maximo  = nombre
                genero_maximo  = genero
                bandera_maximo = False

            
            #2. Promedio de dinero ganado en Ruleta. 
                match juego:
                    case "Poker":
                        contador_poker +=1
                        acumulador_importe_poker += importe_ganado

                        if importe_ganado > importe_maximo_poker or contador_poker == 1:
                            importe_maximo_poker = importe_ganado
                            nombre_maximo_poker = nombre
                    case "Tragamonedas":
                        contador_tragamonedas +=1
                        acumulador_importe_tragamonedas += importe_ganado
                    case "Ruleta":
                        contador_ruleta += 1
                        acumulador_importe_ruleta += importe_ganado


            #5. Promedio de importe ganado de las personas que NO jugaron Poker, 
            #   siempre y cuando el importe supere los $15000
            if juego != "Poker" and importe_ganado > 15000:
                contador_no_poker +=1
                acumulador_importe_no_poker += importe_ganado

        seguir = question("Ingresa otro?")

    #procesos fuera del while
        if contador_ruleta > 0:
            promedio_ganado_ruleta = acumulador_importe_ruleta / contador_ruleta
        else:
            promedio_ganado_ruleta = "No se ingreso ruleta"

    #3. Porcentaje de personas que jugaron en el Tragamonedas.
        cantidad_ganadores = contador_tragamonedas + contador_poker + contador_ruleta
        porcentaje_tragamonedas = (contador_tragamonedas * 100) / cantidad_ganadores

    #4.
        if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
            menos_jugado = "Poker"
        elif contador_ruleta < contador_tragamonedas :
            menos_jugado = "Ruleta"
        else:
            menos_jugado = "Tragamonedas"

        if contador_no_poker > 0:
            promedio_no_poker = acumulador_importe_no_poker / contador_no_poker
        else:
            promedio_no_poker = "Todos jugaron poker"

        #6.
        total_acumulado = acumulador_importe_poker + acumulador_importe_tragamonedas + acumulador_importe_ruleta

        porcentaje_total_poker = (acumulador_importe_poker * 100) / total_acumulado
        porcentaje_total_tragamonedas = (acumulador_importe_tragamonedas * 100) / total_acumulado
        porcentaje_total_ruleta = (acumulador_importe_ruleta * 100) / total_acumulado

        

        #salidas
        print(f"1. Nombre y género de la persona que más ganó. {importe_maximo} {nombre_maximo} {genero_maximo}")
        print(f"2. Promedio de dinero ganado en Ruleta. {promedio_ganado_ruleta}")
        print(f"3.{porcentaje_tragamonedas}")
        print(f"4. {menos_jugado}")
        print(f"5. {promedio_no_poker}")
        print(f"6. {porcentaje_total_poker} {porcentaje_total_tragamonedas} {porcentaje_total_ruleta}")

        #7.
        if contador_poker > 0:
            print(f"{importe_maximo_poker} {nombre_maximo_poker}")
        else:
            print("Nadie jugo al poker para calcular el maximo... ")


  
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
