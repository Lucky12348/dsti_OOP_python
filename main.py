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
        try:
            if command == "1":
                description = input("description: ")
                programmer_name, estimated_time = input("programmer and workload estimate: ").split()
                orders.add_order(description, programmer_name, int(estimated_time))
                print("added!")
            elif command == "2":
                if not orders.all_orders(True):
                    print("no finished tasks")
                for order in orders.all_orders(True):
                    print(order)
            elif command == "3":
                if not orders.all_orders():
                    print("no unfinished tasks")
                for order in orders.all_orders():
                    print(order)
            elif command == "4":
                order_id = input("id: ")
                orders.mark_finished(int(order_id))
                print("marked as finished!")
            elif command == "5":
                if not orders.programmers():
                    print("no programmers")
                for programmers in orders.programmers():
                    print(programmers)
            elif command == "6":
                programmer_name = input("programmer: ")
                status = orders.status_of_programmer(programmer_name)
                print(f"task : finished {status[0]},",
                    f"not finished {status[1]},",
                    f"hours: done {status[2]},",
                    f"scheduled {status[3]}")
            else:
                print(f"'{command}' command not exist")
            command = input("command: ")
        except ValueError:
            print("erroneous input")
            command = input("command: ")


if __name__ == "__main__":
    main()
