import tkinter as tk
from tkinter import messagebox

class Janela_Exemplo:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Meu primeiro sisteminha")
        self.janela.geometry("1200x800")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#1D6BAC")
        self.configurar_janela()
        
    def configurar_janela(self):
     # TITULO #
        self.lbl_titulo = tk.Label(
            self.janela,
            text= "EXEMPLO DE CADASTRO",
            font= ("Arial", 12, "bold")
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            padx= 10,
            pady = 5,
            columnspan= 3
        )
        
        
        #DADOS DA JANELA
        self.frm_dados = tk.Frame(
            self.janela,
            padx = 10,
            pady = 5,
            bg = "#f3f6f8"
        )
        self.frm_dados.grid(
            row= 1,
            column= 0
        )
        self.frm_botoes = tk.Frame(
            self.janela,
            padx = 10,
            pady = 5,
            bg = "#fd0000",
            borderwidth= 2,
            relief= "solid"
        )
        self.frm_botoes.grid(
            row= 2,
            column= 0
        )
        
        
        # NOME #
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = "Nome: "
            
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = 5
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 30
        )
        self.txt_nome.grid(
            row = 1,
            column = 1
        )   
        
        
        # IDADE #
        self.lbl_idade = tk.Label(
            self.frm_dados,
            text = "Idade: "
        )
        self.lbl_idade.grid(
            row = 3,
            column = 0,
            padx = 10,
            pady = 5
        )
        self.txt_idade = tk.Entry(
            self.frm_dados,
            width= 30
        )
        self.txt_idade.grid(
            row = 3,
            column = 1
        )
        
        
        #BTN NOME
        btn_escrever_nome = tk.Button(
            self.frm_botoes,
            text= "Printar o nome",
            command = self.printar()
        )
        btn_escrever_nome.grid(
            row= 2,
            column= 1,
            padx= 10,
            pady = 5
        )       
        
        
        #BTN IDADE
        self.btn_avaliar_idade = tk.Button(
            self.frm_botoes,
            text = "Avaliar idade",
            command= self.avaliar_idade()
        )
        self.btn_avaliar_idade.grid(
            row = 4,
            column= 1
        )

    def printar(self):
        print(self.txt_nome.get())
        
        
    def avaliar_idade(self):
        if self.txt_idade.get() == "":
            messagebox.showerror(
                "Sisteminha",
                "Cara de cu, tem alguém ai ? Esta vivo ?"
            )
            return    
        idade = int(self.txt_idade.get())
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

# MAIN #
    def iniciar(self):
        self.configurar_janela()
        self.janela.mainloop()

janelao = Janela_Exemplo()
janelao.iniciar()

