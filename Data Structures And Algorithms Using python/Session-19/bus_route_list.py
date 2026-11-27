# Task 1.Write 'bus_route_list.py' in a folder named 'bus_route_list' with a class `Node` holding
#  `stop_name` and `next` (starting as None) and a class `BusRoute` with `head` set to None and
#  a method `add_stop(stop_name)` that adds a new node at the end by walking to the last node.
#  Add 5 Ahmedabad stops of your choice, then print the head's stop name and the name of the stop after it.


l1 = ["Maninagar","Kalupur","Lal Darwaja","Paldi","Nehrunagar"]

class node:
    def __init__(self,head):
        self.head = []
        self.next = None
    