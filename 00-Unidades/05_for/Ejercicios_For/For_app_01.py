import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        for i in range(5):
            alert("UTN",i+1)

        print("FIN")
        
        #limite = 10

        #rango = list(range(3, limite))   #range(a,b,c) a = donde empieza, b= donde termina, c=cuanto escala segun iteracion. range(0,10,2)

        #print(rango)

        #while: no conocemos la cantidad de iteraciones 
        #for: conoecemos la cantidad de iteraciones
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()