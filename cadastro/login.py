# importando o TKINTER
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label
from tkinter import messagebox
import menu


def validar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()


    if usuario == "admin" and senha == "123456":
        label_mensagem = Label(tela, text="Liberado", foreground="#008000")
        label_mensagem.place(x=130, y=72)
        tela.after(600,(tela.destroy(), menu.iniciar_menu()))

    else:
        label_mensagem = Label(tela, text="Negado", foreground="#FF0000")
        label_mensagem.place(x=130, y=72)
        entry_usuario.delete(0, END)
        entry_senha.delete(0, END)
        tela.after(1200, lambda:label_mensagem.config(text=""))


tela= Tk()
tela.title("Login")
tela.geometry("300x150")
tela.config(background="#3f4742")

frame_login = Frame(tela, width=300, height=300)
frame_login.grid(row=3, column=2)

label_usuario= Label(frame_login, text="Usuário:", font=('Ivy 12'))
label_usuario.place(x=20, y=25)
entry_usuario = Entry(frame_login)
entry_usuario.place(x=90, y=28)

label_senha= Label(frame_login, text="Senha:", font=('Ivy 12'))
label_senha.place(x=20, y=50)
entry_senha= Entry(frame_login, show="*")
entry_senha.place(x=90, y=52)

label_acesso= Label(frame_login, text="acesso: ")
label_acesso.place(x=90, y=72)


b_entrar = Button(frame_login, command=validar,text="Entrar", width=6, height=1)
b_entrar.place(x=120, y=100)

tela.mainloop()