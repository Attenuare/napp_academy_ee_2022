from engine.ordenationengine import OrganizedEngine
from engine.structures.client import Client


def main():
    '''
        main method to control
        the objects relation
    '''
    print('\n', 10 * ' - ', " Attenuare's Cafeteria ", 10 * ' - ', '\n')
    all_clients = []
    all_orders = []
    while True:
        print('\n\t[1] - Enter cafeteria\n\t[2] - See all clients\n\t[3] - See all orders\n\t[4] - Find client by name')
        primordial_choice = int(input('Choice: '))
        if primordial_choice == 1:  # Entering cafeteria
            decision = str(input('Do you want to order? => [Y] or [N] \nChoice: ')).strip()
            if decision.lower() == 'y':
                next_client = 1
                next_request = 1
                client = str(input('Enter your name and lastname: ')).strip()
                engine = OrganizedEngine(all_clients, 'c')
                searching_client = engine.find_client_by_name(client)
                if searching_client != 0:  # Ordering with a client already with a registration
                    order = engine.ordering(next_request)
                    next_request += 1
                else:  # Client that still doesn't have a registration
                    print("\nYou does'n have a registration!")
                    name = str(input('Enter your full name: ')).strip()
                    age = int(input('Enter your age: '))
                    order = engine.ordering(next_request)
                    client = Client(next_client, name, age, next_request)
                    order.gettotalvalue()
                    all_clients.append(client)
                    all_orders.append(order)
                    next_request += 1
                    next_client += 1
            if decision.lower() == 'n':
                print("Okay, thanks for passing trought Attenuare's cafeteria!")
                break
        if primordial_choice == 2:
            print('\n', 10 * ' - ', " All Clients ", 10 * ' - ', '\n')
            if len(all_clients) > 0:
                for client in all_clients:
                    print('\n', 'Name: ', client.name, '\n\t', 'Age: ', client.age, '\n\t', 'Order: ', client.request_id)
                    if client.is_senior:
                        print('This client is a Senior!')
            else:
                print('The cafeteria is empty!')
        if primordial_choice == 3:
            print('\n', 10 * ' - ', " All Orders ", 10 * ' - ', '\n')
            for order in all_orders:
                print('\n', 'Order: : ', order.id_, '\n\t', 'Has : ', order.itenscount, ' itens\n\t', 'Total: ', order.total)


if __name__ == '__main__':
    main()
