class ConcurrencyConflictError(Exception):

    def __init__(self, message="Conflito de concorrência"):
        self.message = message
        super().__init__(self.message)


class OverbookingError(Exception):

    def __init__(self, message="Não há assentos disponíveis"):
        self.message = message
        super().__init__(self.message)


class RoomUnavailableError(Exception):

    def __init__(self, message="Quarto indisponível para o período"):
        self.message = message
        super().__init__(self.message)