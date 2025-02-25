from task import OrderBook
import os


def main():
    orders = OrderBook()
    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ====================================================\n",
          "========= welcome to the DSTI task manager =========\n",
          "====================================================\n\n",
          "enter the command you want to execute :)\n",
          "0: exit\n",
          "1: add order\n",
          "2: list finished tasks\n",
          "3: list unfinished tasks\n",
          "4: mark tasks as finished\n",
          "5: programmers\n",
          "6: status of programmer\n")

    command = input("command: ")
    while command != "0":
        if command == "1":
            description = input("description: ")
            programmer_name, estimated_time = input("programmer and workload estimate: ").split()
            orders.add_order(description, programmer_name, int(estimated_time))
            print("added!")
        elif command == "2":
            if not orders.all_orders():
                print("no finished tasks")
            for order in orders.all_orders():
                print(order)
            # for order in orders.all_orders():
            #     print(order)
        elif command == "3":
            pass
            # for order in orders.all_orders():
            #     print(order)
        elif command == "4":
            pass
            # order_id = int(input("order id: "))
            # orders.mark_finished(order_id)
        elif command == "5":
            pass
            # for programmer in orders.programmers():
            #     print(programmer)
        elif command == "6":
            pass
            # programmer_name = input("programmer name: ")
            # status = orders.status_of_programmer(programmer_name)
            # print(status)
        else:
            print(f"'{command}' command not exist")
        command = input("command: ")


if __name__ == "__main__":
    main()




















# orders = OrderBook()
# orders.add_order("create the backend + BDD", "Abi", 5)
# orders.add_order("make cofee for John", "Abi", 3)
# orders.add_order("analyse and clean the datasets", "John", 10)
# orders.add_order("create the ML", "John", 20)
# orders.add_order("make cofee for Abi", "John", 30)
# orders.add_order("deploy the application", "Abi", 2)

# for order in orders.all_orders():
#     print(order)

# # task 2
# for programmers in orders.programmers():
#     print(programmers)

# dict_orders = orders.dictionnary()
# print(dict_orders['Abi'])

# # print("Marking task finished")
# orders.mark_finished(1)
# # orders.mark_finished(2)
# orders.mark_finished(3)
# # orders.mark_finished(4)

# # print("all unfinished tasks")
# # for order in orders.all_orders():
# #     print(order)

# status = orders.status_of_programmer("John")
# print(status)
