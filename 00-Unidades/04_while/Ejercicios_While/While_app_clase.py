import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #X 2) - Tecnología que mas se votó.
    #X 3) - Porcentaje de empleados por cada genero
    #X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True
        contador_masculino_IOT_AI = 0

        contador_IA    = 0
        contador_IOT   = 0
        contador_RV_RA = 0

        contador_masculino = 0
        contador_femenino  = 0
        contador_otro      = 0

        contador_iot_edad  = 0

        contador_femenino_IA = 0
        acumulador_edades_femeninos_IA = 0
        bandera_minima_edad = False

        minima_edad = 0


        while seguir == True:
            #ingreso de datos y validaciones
            
            # * nombre del empleado
            # * edad (no menor a 18)
            # * genero (Masculino - Femenino - Otro)
            # * tecnologia (IA, RV/RA, IOT)  
            nombre = prompt("Nombre", "Ingrese el nombre")
            edad   = prompt("Nombre", "Ingrese la edad")  
            edad   = int(edad)
            while edad < 18:
                edad   = prompt("Error", "Reingrese la edad")  
                edad   = int(edad)

            genero = prompt("Genero","Ingrese genero: Masculino - Femenino - Otro")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error","Reingrese genero: Masculino - Femenino - Otro")   

            tecnologia = ("Tecnologia","Ingrese tecnologia: IA, RV/RA, IOT")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("Error","Reingrese Tecnologia: IA - RV/RA - IOT") 


            # 2) - Tecnologia que mas se voto
            match tecnologia:
                case "IOT":
                    contador_IOT += 1
                    # 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if edad > 18 and edad < 25 or edad > 33 and edad < 42:
                        contador_iot_edad += 1
                case "IA":
                    contador_IA += 1
                case _:
                    contador_RV_RA += 1
                    #6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                    if bandera_minima_edad == False or edad < minima_edad:
                        minima_edad         = edad
                        nombre_minima_edad  = nombre
                        genero_minima_edad  = genero
                        bandera_minima_edad = True


            #  3) Porcentaje de empleados por cada genero
                    
            match genero:
                case "Masculino":
                    contador_masculino += 1
                     #X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                    if (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <= 50):
                        contador_masculino_IOT_AI += 1
                case "Femenino":
                    contador_femenino += 1
                    #5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if tecnologia == "IA":  
                        contador_femenino_IA += 1
                        acumulador_edades_femeninos_IA += edad

                case "Otro":
                    contador_otro += 1

            #Procesamiento de datos dentro del while


            seguir = question("Seguir", "Desea continuar?")
        
        #procesamiento de datos fuera del while
        # 2) - Tecnologia que mas se voto
        if   contador_IA > contador_RV_RA and contador_IA > contador_IOT:
            print("Se voto mas IA")
        elif contador_RV_RA > contador_IOT:
            print("Se voto mas RV/RA")
        else:
            print("Se voto mas IOT")
            
        #  3) Porcentaje de empleados por cada genero
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_masculinos = (contador_masculino * 100) / total_empleados
        porcentaje_femeninos = (contador_femenino * 100) / total_empleados
        # porcentaje_otro = (contador_otro * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_masculinos + porcentaje_femeninos)

        porcentaje_iot_rango = contador_iot_edad * 100 / contador_IOT

        #5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        if contador_femenino_IA > 0:
            promedio_edades_femenino_IA = acumulador_edades_femeninos_IA / contador_femenino_IA
        else:
            promedio_edades_femenino_IA = "No se ingreso un femenino que cumpla la condicion"

        #Salidas (Informes)
        print(f"1. Cantidad empleados masculinos IOT/IA entre 25 y 50: {contador_masculino_IOT_AI}")
        print(f"2.  ")
        print(f"3. Porcentajes: \n\tFemenino:{porcentaje_femeninos}% \n\tMasculino:{porcentaje_masculinos}% \n\tOtro:{porcentaje_otro}%")
        print(f"4. Porcentajes iot: {porcentaje_iot_rango}")
        print(f"5. Promedio edad fem IA: {promedio_edades_femenino_IA}")
        print(f"6. wawa: {nombre_minima_edad} {genero_minima_edad}")



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
