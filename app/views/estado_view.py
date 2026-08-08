from app.models.estado import Estado

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Estado_View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()


    def configurar_janela(self):

        self.root.title("✨ Estado Ultimate Edition ✨")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Fundo estilo Windows Vista Aero
        self.root.configure(
            bg="#0b5fa5"
        )

    def criar_componentes(self):

        # ==========================
        # TÍTULO
        # ==========================

        self.lbl_titulo = tk.Label(
            self.root,
            text="🌎 Estado Manager",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#0b5fa5"
        )

        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=5,
            pady=15
        )
        
        # ==========================
        # ÁREA DOS DADOS
        # ==========================

        self.frm_dados = tk.LabelFrame(
            self.root,
            text="📋 Dados do Estado",
            font=("Segoe UI", 10, "bold"),
            bg="#dceeff",
            fg="#084c85",
            bd=2,
            relief="groove"
        )

        self.frm_dados.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="ew"
        )

        self.frm_dados.grid_columnconfigure(
            0,
            weight=0
        )

        self.frm_dados.grid_columnconfigure(
            1,
            weight=1
        )
        # ID

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
        # Nome

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
            width=30,
            font=("Segoe UI", 10)
        )

        self.txt_nome.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        # Sigla

        self.lbl_sigla = tk.Label(
            self.frm_dados,
            text="Sigla:",
            bg="#dceeff",
            font=("Segoe UI", 10)
        )

        self.lbl_sigla.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_sigla = tk.Entry(
            self.frm_dados,
            width=5,
            font=("Segoe UI", 10)
        )

        self.txt_sigla.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        # ==========================
        # BOTÕES
        # ==========================

        self.frm_botoes = tk.Frame(
            self.frm_dados,
            bg="#dceeff",
            border=2,
            relief="groove"
        )

        self.frm_botoes.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
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
        # TABELA DE ESTADOS
        # ==========================

        self.tbl_estados = ttk.Treeview(
            self.root,
            height=12
        )

        self.tbl_estados.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Barra de status estilo Windows

        self.lbl_status = tk.Label(
            self.root,
            text="🟢 Sistema iniciado | Aero Mode ativado",
            anchor="w",
            fg="white",
            bg="#084c85",
            font=("Segoe UI", 9)
        )

        self.lbl_status.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew"
        )



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


        self.tbl_estados.configure(
            style="Vista.Treeview"
        )



        self.tbl_estados["columns"] = (
            "id",
            "nome",
            "sigla"
        )


        self.tbl_estados.column(
            "#0",
            width=0,
            stretch=False
        )


        self.tbl_estados.column(
            "id",
            width=50,
            anchor="center"
        )


        self.tbl_estados.column(
            "nome",
            width=300
        )


        self.tbl_estados.column(
            "sigla",
            width=100,
            anchor="center"
        )



        self.tbl_estados.heading(
            "id",
            text="ID"
        )


        self.tbl_estados.heading(
            "nome",
            text="Nome do Estado"
        )


        self.tbl_estados.heading(
            "sigla",
            text="Sigla"
        )
    def configurar_eventos(self):

        self.btn_novo.config(
            command=self.controller.new
        )
        self.btn_salvar.config(
            command=self.controller.save
        )
        self.btn_alterar.config(
            command=self.controller.update
        )
        self.btn_excluir.config(
            command=self.controller.delete
        )
        self.btn_fechar.config(
            command=self.fechar
        )
        self.tbl_estados.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_estado
        )


    def preencher_campos(self, estado):

        self.limpar_campos()


        self.txt_id.config(
            state="normal"
        )


        self.txt_id.insert(
            0,
            str(estado.id)
        )


        self.txt_id.config(
            state="readonly"
        )


        self.txt_nome.insert(
            0,
            estado.nome
        )


        self.txt_sigla.insert(
            0,
            estado.sigla
        )



    def limpar_campos(self):

        self.txt_id.config(
            state="normal"
        )


        self.txt_id.delete(
            0,
            tk.END
        )


        self.txt_id.config(
            state="readonly"
        )


        self.txt_nome.delete(
            0,
            tk.END
        )


        self.txt_sigla.delete(
            0,
            tk.END
        )


        self.txt_nome.focus()



    def limpar_treeview(self):

        for item in self.tbl_estados.get_children():

            self.tbl_estados.delete(
                item
            )



    def get_id_selecionado(self):

        selecionado = self.tbl_estados.selection()

        if not selecionado:
            return None
        item = self.tbl_estados.item(
            selecionado[0]
        )
        return item["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação Vista",
            "Deseja realmente excluir este estado? 🗑"
        )

    def ler_dados_estado(self):

        nome = self.txt_nome.get()

        sigla = self.txt_sigla.get()


        return nome, sigla



    def exibir_mensagem(self, mensagem, sucesso=True):

        if sucesso:

            messagebox.showinfo(
                "Estado Vista Ultimate",
                mensagem
            )

        else:

            messagebox.showerror(
                "Estado Vista Ultimate",
                mensagem
            )



    def exibir_estados(self, estados):

        self.limpar_treeview()


        for estado in estados:

            self.tbl_estados.insert(
                "",
                tk.END,
                values=(
                    estado.id,
                    estado.nome,
                    estado.sigla
                )
            )


        self.lbl_status.config(
            text=f"🟢 {len(estados)} estados carregados | Sistema funcionando perfeitamente"
        )



    def fechar(self):

        resposta = messagebox.askyesno(
            "Estado Vista",
            "Deseja fechar o sistema?"
        )


        if resposta:

            self.root.destroy()



    def iniciar(self):

        self.controller.get_all()