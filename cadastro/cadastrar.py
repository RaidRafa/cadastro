from tkinter import *

def iniciar_cadastro():
    # Define a função salvar_dados aqui
    def salvar_dados():
        # Coletando dados das entradas
        nome = ent_nome.get()
        cpf = ent_cpf.get()
        rg = ent_rg.get()
        endereco = ent_endereco.get()
        nascimento = ent_nascimento.get()
        instituicao1 = ent_instituicao1.get()
        instituicao2 = ent_instituicao2.get()
        instituicao3 = ent_instituicao3.get()
        cep = ent_cep.get()
        pis = ent_pis.get()
        cargo = ent_cargo.get()
        hora_inicio = ent_hora.get()
        hora_fim = ent_hora2.get()
        exp1 = ent_exp.get()
        exp2 = ent_exp2.get()
        exp3 = ent_exp3.get()

        # Nome do arquivo será o CPF
        nome_arquivo = f"{cpf}.txt"

        # Salva os dados em um arquivo nomeado pelo CPF
        with open(nome_arquivo, "w") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"CPF: {cpf}\n")
            file.write(f"RG: {rg}\n")
            file.write(f"Endereço: {endereco}\n")
            file.write(f"Nascimento: {nascimento}\n")
            file.write(f"Instituição 1: {instituicao1}\n")
            file.write(f"Instituição 2: {instituicao2}\n")
            file.write(f"Instituição 3: {instituicao3}\n")
            file.write(f"CEP: {cep}\n")
            file.write(f"PIS: {pis}\n")
            file.write(f"Cargo: {cargo}\n")
            file.write(f"Horário: {hora_inicio} às {hora_fim}\n")
            file.write(f"Experiência 1: {exp1}\n")
            file.write(f"Experiência 2: {exp2}\n")
            file.write(f"Experiência 3: {exp3}\n")

        # Imprime no console para verificação
        print(f"Dados salvos em {nome_arquivo}")

        # Fecha a janela após salvar
        cadastro.destroy()

    def cancel():
        cadastro.destroy()

    global cadastro  # Torna a variável `cadastro` global
    cadastro = Tk()
    cadastro.title("Cadastro")
    cadastro.geometry("600x700")
    cadastro.config(background="#3f4742")

    frame_cadastro = Frame(cadastro, width=600, height=700)
    frame_cadastro.grid(row=0, column=0)

    Label(cadastro, text="NOME:", width=5, height=5, font=('Ivy 12')).place(x=138, y=2)
    global ent_nome
    ent_nome = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_nome.place(x=192, y=40)

    Label(cadastro, text="CPF:", width=4, height=1, font=('Ivy 12')).place(x=150, y=70)
    global ent_cpf
    ent_cpf = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_cpf.place(x=192, y=72)

    Label(cadastro, text="RG:", width=2, height=1, font=('Ivy 12')).place(x=164, y=101)
    global ent_rg
    ent_rg = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_rg.place(x=192, y=103)

    Label(cadastro, text="ENDEREÇO:", width=10, height=1, font=('Ivy 12')).place(x=94, y=131)
    global ent_endereco
    ent_endereco = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_endereco.place(x=192, y=133)

    Label(cadastro, text="NASCIMENTO:", width=11, height=1, font=('Ivy 12')).place(x=84, y=161)
    global ent_nascimento
    ent_nascimento = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_nascimento.place(x=192, y=163)

    Label(cadastro, text="ESCOLARIDADE:", width=14, height=1, font=('Ivy 12')).place(x=58, y=190)
    Checkbutton(cadastro, text="Ensino Médio").place(x=270, y=190)
    Checkbutton(cadastro, text="Superior").place(x=270, y=215)
    Checkbutton(cadastro, text="Curso Técnico").place(x=270, y=240)

    Label(cadastro, text="INSTITUIÇÂO 1:", width=13, height=1, font=('Ivy 12')).place(x=68, y=270)
    global ent_instituicao1
    ent_instituicao1 = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_instituicao1.place(x=192, y=272)

    Label(cadastro, text="INSTITUIÇÂO 2:", width=13, height=1, font=('Ivy 12')).place(x=68, y=300)
    global ent_instituicao2
    ent_instituicao2 = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_instituicao2.place(x=192, y=301)

    Label(cadastro, text="INSTITUIÇÂO 3:", width=13, height=1, font=('Ivy 12')).place(x=68, y=331)
    global ent_instituicao3
    ent_instituicao3 = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_instituicao3.place(x=192, y=331)

    Label(cadastro, text="CEP:", width=4, height=1, font=('Ivy 12')).place(x=145, y=360)
    global ent_cep
    ent_cep = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_cep.place(x=192, y=361)

    Label(cadastro, text="PIS:", width=4, height=1, font=('Ivy 12')).place(x=150, y=390)
    global ent_pis
    ent_pis = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_pis.place(x=192, y=391)

    Label(cadastro, text="CARGO:", width=6, height=1, font=('Ivy 12')).place(x=125, y=420)
    global ent_cargo
    ent_cargo = Entry(frame_cadastro, width=30, font=('Ivy 12'))
    ent_cargo.place(x=192, y=421)

    Label(cadastro, text="HORÁRIO:", width=8, height=1, font=('Ivy 12')).place(x=110, y=450)
    Label(cadastro, text="DAS:", width=4, height=1, font=('Ivy 12')).place(x=200, y=450)
    global ent_hora
    ent_hora = Entry(frame_cadastro, width=4, font=('Ivy 12'))
    ent_hora.place(x=243, y=451)
    Label(cadastro, text="ÁS:", width=3, height=1, font=('Ivy 12')).place(x=290, y=450)
    global ent_hora2
    ent_hora2 = Entry(frame_cadastro, width=4, font=('Ivy 12'))
    ent_hora2.place(x=323, y=451)

    Label(cadastro, text="EXPERIÊNCIA 1:", width=13, font=('Ivy 12')).place(x=65, y=480)
    global ent_exp
    ent_exp = Entry(cadastro, width=30, font=('Ivy 12'))
    ent_exp.place(x=192, y=482)

    Label(cadastro, text="EXPERIÊNCIA 2:", width=13, font=('Ivy 12')).place(x=65, y=510)
    global ent_exp2
    ent_exp2 = Entry(cadastro, width=30, font=('Ivy 12'))
    ent_exp2.place(x=192, y=512)

    Label(cadastro, text="EXPERIÊNCIA 3:", width=13, font=('Ivy 12')).place(x=65, y=540)
    global ent_exp3
    ent_exp3 = Entry(cadastro, width=30, font=('Ivy 12'))
    ent_exp3.place(x=192, y=542)

    Label(cadastro, text="CONTRATO:", width=10, font=('Ivy 12')).place(x=95, y=580)
    Button(cadastro, text="Inserir arquivo", font=('Ivy 12'), width=12, height=1).place(x=240, y=578)

    # Botão de salvar que chama a função `salvar_dados`
    Button(cadastro, command=salvar_dados, text="Salvar", width=6, height=1, font=('Ivy 12')).place(x=450, y=660)

    # Botão de cancelar
    Button(cadastro, command=cancel, text="Cancelar", width=6, height=1, font=('Ivy 12')).place(x=520, y=660)

    cadastro.mainloop()

# Chamada para iniciar o cadastro
iniciar_cadastro()