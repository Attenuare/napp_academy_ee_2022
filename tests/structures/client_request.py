

class ClientRequest():
    '''
    { structure request }
    Request made by the client
    with all his information
    '''
    def __init__(self, id_: int, all_itens: list[dict[str: str]]) -> None:
        self.id_ = id_
        self.all_itens = all_itens
        self.itenscount = len(all_itens)
        self.total = 0
        self.request_rate = int()
        self._paid = False

    def get_payment_situation(self):
        return self._paid

    def gettotalvalue(self) -> None:
        for item in self.all_itens:
            self.total += item['value']

    def output_request_information(self):
        print('\n', 'Order: : ', self.id_, '\n\t', 'Has : ', self.itenscount, ' itens\n\t', 'Total: ', self.total)
        print('Avaliation: ', self.request_rate * '*')

    def payment(self):
        payment = self.total
        options = {1: 'Debit', 2: 'Credit', 3: 'Cash'}
        while True:
            print('Amount left: ', payment)
            print('Options of payment: \n\t[1] - Debit\n\t[2] - Credit\n\t[3] - Cash')
            decision = int(input('Choice: '))
            if decision not in list(options.keys()):
                print('Wrong choice! Try again!')
                continue
            else:
                while True:
                    value = float(input(f'How much your gonna pay in {options[decision]}?\n\tAmount: '))
                    if value > float(payment):
                        print('The amount is bigger then the order total!')
                        continue
                    else:
                        payment = payment - value
                        break
                if payment == 0:
                    self._paid = True
                    print('Payment completed!')
                    break

    def get_avaliation(self):
        while True:
            avaliations = [1, 2, 3, 4, 5]
            print('Rate the service: ')
            avaliation = int(input('\n\t[1] - Terrible\n\t[2] - Bad\n\t[3] - Neutral\n\t[4] - Good\n\t[5] - Excellent\nChoice: '))
            if avaliation not in avaliations:
                print('Wrong choice! Try again!')
            else:
                self.request_rate = avaliation
                print('Thanks for the avaliation!')
                break
