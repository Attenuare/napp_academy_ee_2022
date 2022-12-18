from structures.ordenationengine import OrganizedEngine
from structures.client_request import ClientRequest
from structures.client import Client


class Test_client:

    def test_client_defined(self):
        self.first_client = Client(0, 'steven', 12, 1)
        self.second_client = Client(1, 'mary', 82, 2)
        assert isinstance(self.first_client, Client)
        assert isinstance(self.second_client, Client)

    def test_client_attributes_verification(self):
        self.test_client_defined()
        assert isinstance(self.first_client.name, str)
        assert isinstance(self.first_client.age, int)
        assert isinstance(self.second_client.name, str)
        assert isinstance(self.second_client.age, int)

    def test_client_senior_confirmation(self):
        self.test_client_defined()
        assert isinstance(self.first_client.is_senior, bool)
        assert isinstance(self.second_client.is_senior, bool)
        assert self.first_client.is_senior is False
        assert self.second_client.is_senior is True


class Test_client_request(Test_client):

    def test_client_defined_request(self):
        all_itens = [{'item': 'Rice', 'value': 10.0, 'type': 'Food'}, {'item': 'Beans', 'value': 20.20, 'type': 'Food'}]
        self.test_client_defined()
        self.first_request = ClientRequest(1, all_itens)
        self.second_request = ClientRequest(1, all_itens)
        assert isinstance(self.first_request, ClientRequest)
        assert isinstance(self.second_request, ClientRequest)

    def test_client_request_attributes_verification(self):
        self.test_client_defined_request()
        self.first_request.gettotalvalue()
        self.second_request.gettotalvalue()
        assert isinstance(self.first_request.total, float)
        assert isinstance(self.first_request.request_rate, int)
        assert isinstance(self.second_request.total, float)
        assert isinstance(self.second_request.request_rate, int)

    def test_client_request_itens_verification(self):
        self.test_client_request_attributes_verification()
        assert isinstance(self.first_request.all_itens[0], dict)
        assert isinstance(self.first_request.all_itens[0]['item'], str)
        assert isinstance(self.first_request.all_itens[0]['value'], float)
        assert isinstance(self.first_request.all_itens[0]['type'], str)

    def test_client_request_total_verification(self):
        total_value = 0
        self.test_client_request_attributes_verification()
        for item in self.first_request.all_itens:
            total_value += item['value']
        assert total_value == self.first_request.total


class Test_ordenation_engine(Test_client):

    def test_ordenation_engine_defined(self):
        self.test_client_defined()
        self.third_client = Client(2, 'mary', 25, 2)
        self.all_clients = [self.first_client, self.second_client, self.third_client]
        self.engine = OrganizedEngine(self.all_clients, 'c')
        assert isinstance(self.all_clients, list)
        assert isinstance(self.all_clients[2], Client)

    def test_ordenation_engine_confirm_order_before(self):
        self.test_ordenation_engine_defined()
        assert len(self.all_clients) > 0
        assert self.all_clients[0].age == 12
        assert self.all_clients[1].age == 82
        assert self.all_clients[2].age == 25

    def test_ordenation_engine_confirm_is_senior_before(self):
        self.test_ordenation_engine_defined()
        assert len(self.all_clients) > 0
        assert self.all_clients[0].is_senior is False
        assert self.all_clients[1].is_senior is True
        assert self.all_clients[2].is_senior is False

    def test_ordenation_engine_confirm_order_after(self):
        self.test_ordenation_engine_defined()
        self.all_clients = self.engine.organize_clients()
        assert len(self.all_clients) > 0
        assert self.all_clients[0].age == 82
        assert self.all_clients[1].age == 12
        assert self.all_clients[2].age == 25

    def test_ordenation_engine_confirm_is_senior_after(self):
        self.test_ordenation_engine_defined()
        assert len(self.all_clients) > 0
        self.all_clients = self.engine.organize_clients()
        assert self.all_clients[0].is_senior is True
        assert self.all_clients[1].is_senior is False
        assert self.all_clients[2].is_senior is False
