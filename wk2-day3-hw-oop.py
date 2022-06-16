



class Cart:
    

    def __init__(self):
        # instance attributes
        self.cart = []
        
        
    def add(self):
        item = input("What item? ")
        self.cart.append(item)

    def remove(self):
        item_to_remove = input("What would you like to remove? ")
        self.cart.remove(item_to_remove)

    def view(self):
        input(self.cart)

    def choose(self):
        finished = 'no'
            
        while finished == 'no':
            selection = input("""What would you like to do?                 
                Type 'add' to add items to your cart. 
                Type 'remove' to remove items from your cart.
                Type 'view' to view the items in your cart. 
                'Add'/'Remove'/'Vew'? """).lower()

            if selection == "add":
                self.add()
            elif selection == "remove":
                self.remove()
            elif selection == "view":
                self.view()

            finished = input("Are you finished? Type 'yes' or 'no': ").lower()
            if finished == 'yes':
                self.view()


# instantiation
cart1 = Cart()  # new instance
cart1.choose()