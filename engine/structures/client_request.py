

class ClientRequest():
    '''
    Request made by the client
    with all his information
    '''
    def __init__(self, id_: int, all_itens: list[dict[str: str]]) -> None:
        self.id_ = id_
        self.all_itens = all_itens
        self.itenscount = len(all_itens)
        self.total = 0

    def gettotalvalue(self) -> None:
        for item in self.all_itens:
            self.total += item['value']
