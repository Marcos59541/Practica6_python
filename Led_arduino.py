import serial
import tkinter as tk

puerto_serial = serial.Serial("com6", 9600)

def a():
    puerto_serial.write(b'b')
def b():
    puerto_serial.write(b'a')

ventana = tk.Tk()
ventana.title("Hola")

encender = tk.Button(ventana, text= "ON", command= a)
encender.pack(pady=10)

apagar = tk.Button(ventana, text= "OFF", command=b)
apagar.pack(pady=10)


ventana.mainloop()

puerto_serial.close()
