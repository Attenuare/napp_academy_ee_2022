

class Client():
    '''
    { structure client } 
    use to store all information from person 
    that have a contact with the cafeteria
    '''
    def __init__(self, id_: int, name: str, age: int, request_id: int):
        self.id_ = id_
        self.name = name
        self.age = age
        self.is_senior = False
        self.request_id = request_id
        if age > 65:
            self.is_senior = True

    def output_client_information(self):
        print('\n', 'Name: ', self.name, '\n\t', 'Age: ', self.age, '\n\t', 'Order: ', self.request_id)
        if self.is_senior:
            print('This client is a Senior!')
