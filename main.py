from engine.ordenationengine import OrganizedEngine
from engine.structures.client import Client
from time import sleep
from tqdm import tqdm
import os


def main():
    '''
        main method to control
        the objects relation
    '''
    os.system('cls')
    print('\n', 10 * ' - ', " Attenuare's Cafeteria ", 10 * ' - ', '\n')
    all_clients = []  # Clients that just enter the cafeteria, they are waiting to order
    all_orders = []
    client_queue = []  # Clients that already order
    next_client_number = 1
    next_request = 1
    order_controller = {}
    while True:
        print('\n\t[1] - Enter cafeteria\n\t[2] - See all clients in queue to order\n\t[3] - Get next Order\n\t[4] - See all clients waiting for the order\n\t[5] - See all orders\n\t[6] - Delivering order')
        primordial_choice = int(input('Choice: '))
        if primordial_choice == 1:  # Entering cafeteria
            decision = str(input('Do you want to get in line? => [Y] or [N] \nChoice: ')).strip()
            if decision.lower() == 'y':
                client = str(input('Enter your name and lastname: ')).strip()
                engine = OrganizedEngine(all_clients, 'c')
                searching_client = engine.find_client_by_name(client)
                if searching_client != 0:  # Ordering with a client already with a registration
                    print('This client is already in line, on position ', searching_client[1] + 1)
                else:  # Client that still doesn't have a registration
                    print("\nYou does'n have a registration!")
                    engine.new_client()
                    #  order = engine.ordering(next_request)
                    client = Client(next_client_number, engine.next_client['name'], engine.next_client['age'], engine.next_client['request'])
                    #  order.gettotalvalue()
                    all_clients.append(client)
                    #  all_orders.append(order)
                    next_client_number += 1
                    engine = OrganizedEngine(all_clients, 'c')
                    all_clients = engine.organize_clients()
            if decision.lower() == 'n':
                print("Okay, thanks for passing trought Attenuare's cafeteria!")
                break
        if primordial_choice == 2:
            os.system('cls')
            print('\n', 10 * ' - ', " All Clients [Before ordering]", 10 * ' - ', '\n')
            if len(all_clients) > 0:
                for client in all_clients:
                    client.output_client_information()
            else:
                print('The cafeteria is empty!')
        if primordial_choice == 3:
            if len(all_clients) > 0:
                os.system('cls')
                print('Serving next Customer')
                print('\tCustumer ', all_clients[0].name)
                client_queue.append(all_clients[0])
                all_clients[0].request_id = next_request
                order_controller[f'c_{all_clients[0].id_}'] = client_queue.index(all_clients[0])
                order_controller[f'o_{next_request}'] = all_clients[0].id_
                all_clients = all_clients[1:]
                order = engine.ordering(next_request)
                order.gettotalvalue()
                order.payment()
                order.get_avaliation()
                all_orders.append(order)
                order_controller[f'in_o_{next_request}'] = all_orders.index(order)
                next_request += 1
            else:
                print("There's no client in queue!")
        if primordial_choice == 4:
            os.system('cls')
            print('\n', 10 * ' - ', " All Clients [After ordering]", 10 * ' - ', '\n')
            if len(client_queue) > 0:
                for client in client_queue:
                    client.output_client_information()
            else:
                print('The queue is empty!')
        if primordial_choice == 5:
            os.system('cls')
            print('\n', 10 * ' - ', " All Orders ", 10 * ' - ', '\n')
            for order in all_orders:
                order.output_request_information()
        if primordial_choice == 6:
            os.system('cls')
            order_ready = int(input('Enter order number that is going to be made: '))
            client_order = order_controller.get(f'o_{order_ready}', '-')
            client_index = order_controller.get(f'c_{client_order}', '-')
            if client_index != '-':
                if all_orders[order_controller[f'in_o_{order_ready}']].get_payment_situation():
                    print('Preparing order...')
                    _ = [sleep(1) for _ in tqdm(range(5))]
                    print('Delivering order to Client: ')
                    client_queue[client_index].output_client_information()
                    client_queue.remove(client_queue[client_index])
                else:
                    print(f'The order {order_ready} needs payment!')


if __name__ == '__main__':
    main()
