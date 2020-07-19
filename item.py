class Item:

    def __init__(self, quantity, imported, cost):
        self.quantity = quantity
        self.imported = imported
        self.cost = cost

    def __str__(self):
        return "Quantity: {}, Imported: {}, Cost: {}".format(self.quantity, self.imported, self.cost)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.quantity == other.quantity and
            self.imported == other.imported and
            self.cost == other.cost
        )
