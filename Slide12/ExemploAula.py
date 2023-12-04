class Repositorio:
    def __init__(self) -> None:
        self.__baseDeDados = {} # Dicionário vazio
    def select(self, nome: str) -> str:
        existe = self.__baseDeDados[nome]
        if existe:
            return f"{nome}, {self.__baseDeDados[nome]}"
        else:
            # Se o nome não existir retorna Vazio
            return None
    def insert(self, nome:str, idade:int) -> str:
        self.__baseDeDados[nome] = idade
        return f"Inserindo dados: {nome} e {idade}"

class RepoFalso_SelectVazio(Repositorio):
    def __init__(self) -> None:
        super().__init__()
        # Método select foi sobrescrito
    def select(self, nome: str) -> str:
        return None

    class RepoFalso_SelectTrue(Repositorio):
        def __init__(self) -> None:
            super().__init__()
            # Método select foi sobrescrito
    def select(self, nome: str) -> str:
        return True