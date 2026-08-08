from app.models.cidade import Cidade


class Cidade_Controller:

    def __init__(self, dao, estado_dao, view):
        self.dao = dao
        self.estado_dao = estado_dao
        self.view = view
        self.estado_selecionado = None

    def new(self):
        self.estado_selecionado = None
        self.view.limpar_campos()

    def carregar_estados(self):
        estados = self.estado_dao.get_all()
        self.view.carregar_estados(estados)

    def selecionar_estado(self, event=None):

        id_cidade = self.view.get_id_selecionado()

        if id_cidade is None:
            return

        cidade = self.dao.get_by_id(id_cidade)

        if cidade is not None:
            self.estado_selecionado = cidade
            self.view.preencher_campos(cidade)

    def save(self):

        try:

            nome, estado = self.view.ler_dados_cidade()

            if self.estado_selecionado is None:

                cidade = Cidade(
                    None,
                    nome,
                    estado
                )

                self.dao.save(cidade)

                self.view.exibir_mensagem(
                    "Cidade cadastrada com sucesso!"
                )

            else:

                self.estado_selecionado.atualizar_dados(
                    nome,
                    estado
                )

                self.dao.update(
                    self.estado_selecionado
                )

                self.view.exibir_mensagem(
                    "Cidade atualizada com sucesso!"
                )

            self.new()
            self.get_all()

        except Exception as e:

            self.view.exibir_mensagem(
                str(e),
                False
            )

    def get_all(self):

        cidades = self.dao.get_all()

        self.view.exibir_cidades(cidades)

    def update(self):

        if self.estado_selecionado is None:

            self.view.exibir_mensagem(
                "Selecione uma cidade.",
                False
            )

            return

        try:

            nome, estado = self.view.ler_dados_cidade()

            self.estado_selecionado.atualizar_dados(
                nome,
                estado
            )

            self.dao.update(
                self.estado_selecionado
            )

            self.view.exibir_mensagem(
                "Cidade atualizada com sucesso!"
            )

            self.new()
            self.get_all()

        except Exception as e:

            self.view.exibir_mensagem(
                str(e),
                False
            )

    def delete(self):

        if self.estado_selecionado is None:

            self.view.exibir_mensagem(
                "Selecione uma cidade.",
                False
            )

            return

        if not self.view.confirmar_exclusao():
            return

        sucesso = self.dao.delete(
            self.estado_selecionado.id
        )

        if sucesso:

            self.view.exibir_mensagem(
                "Cidade excluída com sucesso!"
            )

            self.new()
            self.get_all()

        else:

            self.view.exibir_mensagem(
                "Cidade não encontrada.",
                False
            )

    def inicializar_sistema(self):
        self.view.iniciar()