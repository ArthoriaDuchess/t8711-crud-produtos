import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.estado import Estado

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Estado_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.configurar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        
    def configurar_janela(self):
        self.root.title("CRUD de Estado")
        self.root.geometry("800x600")
        self.root.resizable(False,False)
        
    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Estados",
            font = ("Arial", 16, "Bold")
        )
        self.lbl_titulo.grid(
            row = 0,
            column= 0,
            columnspan= 4,
            padx= 5,
            pady= 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados do estado"
        )
        self.frm_dados.grid(
            row= 1,
            column= 0,
            columnspan= 4,
            padx= 10,
            pady= 5,
            sticky= "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text= "ID: "
        )
        self.lbl_id.grid(
            row= 0,
            column= 0,
            padx= 5,
            pady= 5,
            sticky= "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width= 10,
            state= "readonly"
        )
        self.text_id.grid(
            row= 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky= "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text= "Nome: "
        )
        self.lbl_nome.grid(
            row= 1,
            column= 0,
            padx= 5,
            pady= 5,
            sticky= "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width= 40
        )
        self.text_nome.grid(
            row= 1,
            column= 1,
            padx= 5,
            pady= 5,
            sticky= "w"
        )
        self.lbl_sigla = tk.Label(
            self.frm_dados,
            text= "Sigla: "
        )
        self.lbl_sigla.grid(
            row= 1,
            column= 2,
            padx= 5,
            pady= 5,
            sticky= "w"
        )
        self.txt_sigla = tk.Entry(
            self.frm_dados,
            width= 40
        )
        self.txt_sigla.grid(
            row= 1,
            column= 3,
            padx= 5,
            pady= 5,
            sticky= "w"
        )
    def configurar_treeview(self):
        self.lbl_estados["columns"] = (
            "id",
            "nome",
            "sigla"
        )
        self.tbl_fornecedores.column(
            "#0",
            width= 0,
            stretch = False
        )
        self.tbl_estados.column(
            "id",
            width= 10
        )
        self.tbl_estados.column(
            "nome",
            width= 50
        )
        self.tbl_estados.column(
            "sigla",
            width= 20
        )
        self.tbl_estados.heading(
            "id",
            text= "ID"
        )
        self.tbl_estados.heading(
            "nome",
            text= "Nome"
        )
        self.tbl_estados.heading(
            "sigla",
            text= "Sigla"
        )
        
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_estados.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_fornecedores
        )
        
    def preencher_campos(self, estados):
        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert
    
    
    def iniciar(self):
            self.root.mainloop()