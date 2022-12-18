from structures.client_request import ClientRequest


class OrganizedEngine:
    '''
        Used to search into the structures
        and find specific elements
    '''
    def __init__(self, elements: list or dict or None, type_: str) -> None:
        self.elements = elements
        self.type_ = type_
        self.next_client = {'name': '', 'age': ''}

    def organize_clients(self) -> None:
        senior_clients, other_clients = [], []
        if self.type_ == 'c':
            for client in self.elements:
                if client.is_senior:
                    senior_clients.append(client)
                else:
                    other_clients.append(client)
            senior_clients.extend(other_clients)
            return senior_clients

    def find_client_by_name(self, name: str) -> list[object, int] or int:
        for client in self.elements:
            if name.lower() in client.name:
                return [client, self.elements.index(client)]
        return 0

    def ordering(self, next_request: int):
        order_type = str(input('Enter the type of the order: '))
        all_itens = []
        while True:
            order = str(input('Enter the item: '))
            value = float(input('Enter this item value: '))
            all_itens.append({'item': order, 'value': value, 'type': order_type})
            leave_order = str(input('Do you want do add more items? => [Y] or [N] \nChoice: ')).strip()
            if leave_order.lower() == 'n':
                break
            elif leave_order.lower() == 'y':
                continue
        return ClientRequest(next_request, all_itens)

    def new_client(self):
        name = str(input('Enter your full name: ')).strip()
        age = int(input('Enter your age: '))
        self.next_client['name'] = name
        self.next_client['age'] = age
        self.next_client['request'] = 0
