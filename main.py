import random

###############################################################################
class Node:
    '''ein Listeneintrag der doppelt verketteten Liste mit int als Nutzdaten'''
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

###############################################################################
class DVL:
    '''doppelt verkettete Liste mit int als Nutzdaten'''

    # -------------------------------------------------------------------------
    def __init__(self):
        self.head = None
        # print(repr(self))

    # -------------------------------------------------------------------------
    def append(self, data):
        '''Mehrfacheinträge von data sind erlaubt'''

        assert type(data) == int, "Nutzdaten int!"
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:         # letztes Element suchen
                current = current.next
            current.next = new_node     # vorwärtsverkettung
            new_node.prev = current     # rückwärtsverkettung

    # -------------------------------------------------------------------------
    def append_sorted(self, data):
        new_node = Node(data)

        if not self.head:  # Wenn die Liste leer ist, wird das neue Element das erste Element (der Kopf) der Liste.
            self.head = new_node
        elif data <= self.head.data:  # Wenn das neue Element kleiner oder gleich dem Kopf der Liste ist, wird es zum neuen Kopf.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    # -------------------------------------------------------------------------
    def delete(self, value):
        '''gelöscht wird das erste Auftreten von value vom Kopf an'''

        current = self.head

        # Fall 0: Liste ist leer --> current == None
        # Fall 1: Liste ist nicht leer und  zu löschendes Element ist der Kopf der Liste
        if current and current.data == value:
            if current.next:                # wenn es einen Nachfolger gibt...
                current.next.prev = None    # ...wird dieser neues erstes Element
            self.head = current.next        # das neue erste Element
            current = None                  # Signal zum Verlassen der Schleife
            return

        # Fall 2: Liste ist nicht leer und  zu löschendes  Element ist nicht der Kopf der Liste
        while current:
            if current.data == value:
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                return
            current = current.next

    # -------------------------------------------------------------------------
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    dvl = DVL()
    dvl_sort = DVL()

    # Liste mit 10 zufälligen Werten füllen:
    for _ in range(10):
        n = random.randint(0,100)
        dvl_sort.append_sorted(n)
        dvl.append(n)
    dvl.display()
    dvl_sort.display()

    ...