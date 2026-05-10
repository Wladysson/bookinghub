class DatabaseConnectionError(Exception):

    def __init__(self, message="Erro de conexão com banco de dados"):
        self.message = message
        super().__init__(self.message)


class DatabaseQueryError(Exception):

    def __init__(self, message="Erro ao executar consulta"):
        self.message = message
        super().__init__(self.message)