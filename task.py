# using Pylint for formatting


class Task:
    """PART 1 class to instantiate a task"""
    id = 0

    def __init__(self, description: str = '', estimated_time: int = 0,
                 programmer_name: str = '', status: bool = False):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer_name = programmer_name
        # logic to add good format for estimated_time
        self.estimated_time = estimated_time
        # logic to add good format for status
        self.status = "FINISHED" if status else "NOT FINISHED"

    def __str__(self):
        return (f"{self.id}: {self.description}, ({self.estimated_time} hours)"
                f", {self.programmer_name}, {self.status}")


class OrderBook:
    """PART2 class to manage orders"""

    def __init__(self):
        self.orders = []

    def add_order(self, description: str,  programmer_name: str,
                  estimated_time: int, status: bool = False) -> None:
        """PART2 fuction to add"""
        task = Task(description, estimated_time, programmer_name, status)
        self.orders.append(task)

    def all_orders(self, finished: bool = False):
        """PART2 function return all orders"""
        is_finished = "FINISHED" if finished else "NOT FINISHED"
        # return all false status tasks
        result_order = []
        for order in self.orders:
            if order.status == is_finished:
                result_order.append(order)
        return result_order

    def programmers(self):
        """PART2 function return all programmers"""
        return [order.programmer_name for order in self.orders]

    def dictionnary(self):
        """PART3 function return all orders in a dict key=programmer"""
        result_dict = {}
        # enrich dict
        for order in self.all_orders():
            if order.programmer_name not in result_dict:
                result_dict[order.programmer_name] = []
            result_dict[order.programmer_name].append(
                f"{order.id}: {order.description},"
                f"{order.estimated_time}, {order.status}"
            )
        return result_dict

    def mark_finished(self, order_id: int):
        """PART4 function to update the status to FINISHED"""
        for order in self.orders:
            if order.id == order_id:
                order.status = "FINISHED"
                print(order)
                return order
        raise ValueError("Task not found")

    def status_of_programmer(self, programmer_name: str):
        """PART5 function return tuple sum of unfinish/finish hours"""
        # all hours of programmer
        finish_hours = 0
        unfinish_hours = 0
        # number of tasks
        finish_tasks = 0
        unfinish_tasks = 0
        result = ()
        exist = False
        # enrich hours anf tasks
        for order in self.orders:
            if order.programmer_name == programmer_name:
                exist = True
                if order.status == "FINISHED":
                    finish_hours += order.estimated_time
                    finish_tasks += 1
                else:
                    unfinish_hours += order.estimated_time
                    unfinish_tasks += 1
        if not exist:
            raise ValueError("Programmer not exist")
        result = (finish_tasks, unfinish_tasks, finish_hours, unfinish_hours)
        return result
