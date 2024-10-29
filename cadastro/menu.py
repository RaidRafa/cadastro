# importando o TKINTER
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label

import cadastrar


def abrir_cadastro():
    cadastrar.iniciar_cadastro()

def iniciar_menu():
    print("Menu iniciado!")

    # janela
    janela = Tk()
    janela.title("Cadastrando")
    janela.geometry("1920x1080")

    frame_corpo = Frame(janela, width=1920, height=1080, bg="#2d332f")
    frame_corpo.grid(row=1, column=0)

    b_cadastro = Button(frame_corpo, command=abrir_cadastro,text='Cadastrar', width=50, height=2, bg="#6e6963", font=('Ivy 19'))
    b_cadastro.place(x=600, y=350)

    b_consulta = Button(frame_corpo, text='Consultar', width=50, height=2, bg="#6e6963", font=('Ivy 19'))
    b_consulta.place(x=600, y=450)

    b_deletar = Button(frame_corpo, text='Deletar', width=50, height=2, bg="#6e6963", font=('Ivy 19'))
    b_deletar.place(x=600, y=550)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_menu()
