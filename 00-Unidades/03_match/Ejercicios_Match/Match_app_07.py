import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:   rodrigo
apellido: fleitas
---
Ejercicio: Match_07
---
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        
        destino = self.combobox_destino.get()

        match destino:

            case "Bariloche" :
                mensaje = "¡Este destino esta en el Oeste!"
                alert("UTN", mensaje)
            case "Mar del plata":
                mensaje = "¡Este destino esta en el Este!"
                alert("UTN", mensaje)
            case "Cataratas":
                mensaje = "¡Este destino esta en el Norte!"
                alert("UTN", mensaje)
            case _:   
                mensaje = "¡Este destino esta en el Sur!"
                alert("UTN", mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()