class ResourceNotFoundError(Exception):

    def __init__(self, message="Recurso não encontrado"):
        self.message = message
        super().__init__(self.message)


class ValidationError(Exception):

    def __init__(self, message="Erro de validação"):
        self.message = message
        super().__init__(self.message)


class BusinessRuleError(Exception):

    def __init__(self, message="Regra de negócio violada"):
        self.message = message
        super().__init__(self.message)