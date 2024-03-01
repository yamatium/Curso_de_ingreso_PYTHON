import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:   Rodrigo
apellido: Fleitas
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
        precioPorUnidad = 800

        marca           = self.combobox_marca.get()
        cantidad        = self.combobox_cantidad.get()
        cantidadInt  = int(cantidad)

        precioSinDescuento  = float(precioPorUnidad * cantidadInt)

        #A
        if cantidadInt >= 6:
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.5   
            mensaje = f"Comprando a partir de 6 lamparitas se aplica un descuento de 50%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)
            if precioConDescuento > 4000: 
                precioConDescuentoFinal = precioConDescuento - precioConDescuento * 0.05
                mensaje = f"Con una compra mayor a 4000$ se aplica un descuento de 5%,quedando un total de {precioConDescuentoFinal}"
                alert("ticket de compra", mensaje)
        elif cantidadInt <= 2:
            mensaje = f"Su total es de {precioSinDescuento}"
            alert("Ticket de compra", mensaje)

        #B
        if  cantidadInt == 5 and marca == "ArgentinaLuz" :
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.4
            mensaje = f"Comprando 5 lamparitas ArgentinaLuz se aplica un descuento de 40%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)
        elif cantidadInt == 5:
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.3
            mensaje = f"comprando 5 lamparitas se aplica un descuento de 30%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)

        #C
        if cantidadInt == 4 and  (marca == "ArgentinaLuz" or marca == "FelipeLamparas"): 
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.25
            mensaje = f"Comprando 4 lamparitas ArgentinaLuz o FelipeLamparas se aplica un descuento de 25%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)
        elif cantidadInt == 4 and (marca != "ArgentinaLuz" and marca != "FelipeLamparas"):
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.2
            mensaje = f"Comprando 4 lamparitas se aplica un descuento de 20%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)

        #D
        if cantidadInt == 3 and marca == "ArgentinaLuz":
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.15
            mensaje = f"comprando 3 lamparitas ArgentinaLuz se aplica un descuento de 15%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)
        elif cantidadInt == 3 and marca  == "FelipeLamparas":
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.10
            mensaje = f"Comprando 3 lampartias FelipeLamparas se aplica un descuento de 10%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)
        elif cantidadInt == 3:
            precioConDescuento = precioSinDescuento - precioSinDescuento * 0.05
            mensaje = f"Comprando 3 lamparitas se aplica un descuento de 5%, quedando un total de {precioConDescuento}"
            alert("Ticket de compra", mensaje)

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()