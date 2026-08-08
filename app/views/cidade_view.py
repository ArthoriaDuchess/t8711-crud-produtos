from app.models import estado
from app.models.cidade import Cidade

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Cidade_View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._estados = []

        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("✨Cidade Ultimate Edition ✨")
        self.root.geometry("720x600")
        self.root.resizable(False, False)
        
        self.root.configure(
            bg= "#0b5fa5"
        )

    def criar_componentes(self):
        
        # ==========================
        # TÍTULO
        # ==========================

        self.lbl_titulo = tk.Label(
            self.root,
            text="🌎 Cidade Manager",
            font=("Arial", 16, "bold"),
            fg="White",
            bg="#0b5fa5"
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )
        
        # ==========================
        # ÁREA DOS DADOS
        # ==========================

        self.frm_dados = tk.LabelFrame(
            self.root,
            text="Dados das Cidades",
            font=("Segoe UI", 10, "bold"),
            bg="#dceeff",
            fg="#084c85",
            bd=2,
            relief="groove"
        )
        self.frm_dados.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=10,
            pady=5,
            sticky="ew"
        )

        self.lbl_id = tk.Label(
            self.frm_dados,
            text="ID:",
            bg="#dceeff",
            font=("Segoe UI", 10)
        )
        self.lbl_id.grid(
            row=0, 
            column=0, 
            padx=5, 
            pady=5, 
            sticky="w"
        )

        self.txt_id = tk.Entry(
            self.frm_dados,
            width=10,
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.txt_id.grid(
            row=0, 
            column=1, 
            padx=5, 
            pady=5, 
            sticky="w"
        )
        
        # ==========================
        # NOMES
        # ==========================

        self.lbl_nome = tk.Label(
            self.frm_dados,
            text="Nome:",
            bg="#dceeff",
            font=("Segoe UI", 10)
        )
        self.lbl_nome.grid(
            row=1, 
            column=0, 
            padx=5, 
            pady=5, 
            sticky="w"
        )

        self.txt_nome = tk.Entry(
            self.frm_dados,
            width=40,
            font=("Segoe UI", 10)
        )
        self.txt_nome.grid(
            row=1, 
            column=1, 
            padx=5, 
            pady=5, 
            sticky="w"
        )

        # ==========================
        # ESTADOS
        # ==========================

        self.lbl_estados = tk.Label(
            self.frm_dados,
            text="Estado:",
            bg="#dceeff",
            font=("Segoe UI", 10)
        )
        self.lbl_estados.grid(
            row=1, 
            column=2, 
            padx=5, 
            pady=5, 
            sticky="w"
        )

        self.cmb_estados = ttk.Combobox(
            self.frm_dados,
            width=37,
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.cmb_estados.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="w"
        )

        # ==========================
        # BOTÕES
        # ==========================
        
        self.frm_botoes = tk.Frame(
            self.root,
            bg="#dceeff",
            border=2,
            relief="groove"
        )
        
        self.frm_botoes.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=10,
            pady=5
        )
        
        estilo_botao = {
            "width": 15,
            "font": ("Segoe UI", 10, "bold"),
            "relief": "raised",
            "bd": 2
        }

        self.btn_novo = tk.Button(
            self.frm_botoes,
            text="🆕 Novo",
            bg="#b7e3ff",
            **estilo_botao
        )
        self.btn_novo.grid(
            row=0, 
            column=0, 
            padx=5, 
            pady=5
        )

        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text="💾 Salvar",
            bg="#8fd3ff",
            **estilo_botao
        )
        self.btn_salvar.grid(
            row=0, 
            column=1, 
            padx=5, 
            pady=5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text="✏ Alterar",
            bg="#fff2a8",
            **estilo_botao
        )
        self.btn_alterar.grid(
            row=0, 
            column=2, 
            padx=5, 
            pady=5
        )

        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text="🗑 Excluir",
            bg="#ffaaaa",
            **estilo_botao
        )
        self.btn_excluir.grid(
            row=0, 
            column=3, 
            padx=5, 
            pady=5
        )

        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text="🚪 Fechar",
            bg="#dddddd",
            **estilo_botao
        )
        self.btn_fechar.grid(
            row=0, 
            column=4, 
            padx=5, 
            pady=5
        )

        # ==========================
        # TABELA DE CIDADES
        # ==========================
        
        self.tbl_cidades = ttk.Treeview(
            self.root,
            height=12
        )
        self.tbl_cidades.grid(
            row=3,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )
        
        self.lbl_status = tk.Label(
            self.root,
            text="🟢 Sistema iniciado | Aero Mode ativado",
            anchor="w",
            fg="white",
            bg="#084c85",
            font=("Segoe UI", 9)
        )

        # self.lbl_status.grid(
        #     row=3,
        #     column=0,
        #     columnspan=2,
        #     sticky="ew"
        # )

    def configurar_treeview(self):
        
        estilo = ttk.Style()
        
        estilo.configure(
            "Vista.Treeview",
            font=("Segoe UI", 10),
            rowheight=28
        )


        estilo.configure(
            "Vista.Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )
        
        self.tbl_cidades.configure(
            style= "Vista.Treeview"
        )

        self.tbl_cidades["columns"] = (
            "id",
            "nome",
            "estado"
        )

        self.tbl_cidades.column("#0", width=0, stretch=False)
        self.tbl_cidades.column("id", width=60, anchor="center")
        self.tbl_cidades.column("nome", width=250)
        self.tbl_cidades.column("estado", width=250)

        self.tbl_cidades.heading("#0", text="")
        self.tbl_cidades.heading("id", text="ID")
        self.tbl_cidades.heading("nome", text="Nome")
        self.tbl_cidades.heading("estado", text="Estado")

    def configurar_eventos(self):

        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)

        self.tbl_cidades.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_estado
        )

    def carregar_estados(self, estados):

        self._estados = estados

        valores = [
            f"{estado.id} - {estado.nome}"
            for estado in estados
        ]

        self.cmb_estados["values"] = valores
        self.cmb_estados.set("")

    def preencher_campos(self, cidade):

        self.limpar_campos()

        self.txt_id.config(state="normal")
        self.txt_id.insert(0, cidade.id)
        self.txt_id.config(state="readonly")

        self.txt_nome.insert(0, cidade.nome)

        for indice, estado in enumerate(self._estados):
            if estado.id == cidade.estado.id:
                self.cmb_estados.current(indice)
                break

    def limpar_campos(self):

        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state="readonly")

        self.txt_nome.delete(0, tk.END)

        self.cmb_estados.set("")

        self.txt_nome.focus()

    def limpar_treeview(self):

        for item in self.tbl_cidades.get_children():
            self.tbl_cidades.delete(item)

    def get_id_selecionado(self):

        selecionados = self.tbl_cidades.selection()

        if not selecionados:
            return None

        return self.tbl_cidades.item(
            selecionados[0]
        )["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta cidade?"
        )

    def ler_dados_cidade(self):

        nome = self.txt_nome.get().strip()

        indice = self.cmb_estados.current()

        if indice < 0:
            raise ValueError("Selecione um estado.")

        estado = self._estados[indice]

        return nome, estado

    def exibir_mensagem(self, mensagem, sucesso=True):

        if sucesso:

            messagebox.showinfo(
                "Cidade Vista Ultimate",
                mensagem
            )

        else:

            messagebox.showerror(
                "Cidade Vista Ultimate",
                mensagem
            )

    def exibir_cidades(self, cidades):

        self.limpar_treeview()


        for cidade in cidades:

            self.tbl_cidades.insert(
                "",
                tk.END,
                values=(
                    cidade.id,
                    cidade.nome,
                    cidade.estado.nome
                )
            )


    def fechar(self):

        resposta = messagebox.askyesno(
            "Cidade Vista",
            "Deseja fechar o sistema?"
        )


        if resposta:

            self.root.destroy()

    def iniciar(self):
        self.controller.carregar_estados()
        self.controller.get_all()
        self.root.mainloop()