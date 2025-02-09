import customtkinter  # Import the module
from tkinter import PhotoImage
import os


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Custom Tkinter")
janela.resizable(False, False)

PATH_IMG = "img.png"

if not os.path.exists(PATH_IMG):
    print("Erro: o arquivo não existe")
else:
    print("O arquivo existe")
    img = PhotoImage(file=PATH_IMG)
    label = customtkinter.CTkLabel(master=janela, image=img)
    label.place(x=5, y=65)

janela.mainloop()
