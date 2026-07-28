import tkinter as tk
from tkinter import messagebox

# BASE JANELA #
janela = tk.Tk()

janela.title("Meu primeiro sisteminha")
janela.geometry("1200x800")
janela.resizable(False, False)
janela.configure(bg="#1D6BAC")


# TITULO #
lbl_titulo = tk.Label(
    janela,
    text= "EXEMPLO DE CADASTRO",
    font= ("Arial", 12, "bold")
)

lbl_titulo.grid(
    row = 0,
    column = 0,
    padx= 10,
    pady = 5,
    columnspan= 3
)


# NOME #
lbl_nome = tk.Label(
    janela,
    text = "Nome: "
    
)

lbl_nome.grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)

txt_nome = tk.Entry(
    janela,
    width = 30
)
txt_nome.grid(
    row = 1,
    column = 1
)


# IDADE #
lbl_idade = tk.Label(
    janela,
    text = "Idade: "
)

lbl_idade.grid(
    row = 3,
    column = 0,
    padx = 10,
    pady = 5
)
txt_idade = tk.Entry(
    janela,
    width= 30
)
txt_idade.grid(
    row = 3,
    column = 1
)
def printar():
    print(txt_nome.get())
    
btn_escrever_nome = tk.Button(
    janela,
    text= "Printar o nome",
    command = printar
)
    
btn_escrever_nome.grid(
    row= 2,
    column= 1,
    padx= 10,
    pady = 5
)
def avaliar_idade():
    if txt_idade.get() == "":
        messagebox.showerror(
            "Sisteminha",
            "Cara de cu, tem alguém ai ? Esta vivo ?"
        )
        return    
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo(
            "Sisteminha",
            "Com " + str(idade) + " você é bem vindo"
        )
        return
    messagebox.showwarning(
        "Sisteminha",
        "Seu danadinho!!!!"
    )
    return
        
btn_avaliar_idade = tk.Button(
    janela,
    text = "Avaliar idade",
    command= avaliar_idade
)
btn_avaliar_idade.grid(
    row = 4,
    column= 1
)
# MAIN #
janela.mainloop()
