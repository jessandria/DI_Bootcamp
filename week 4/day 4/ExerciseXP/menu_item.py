
class MenuItem : 
    def __init__(self, item=None, price=None) :
        self.item = item
        self.price = price

    def save(self):
        return print(f"{self.item} - {self.price}")
    
    def delete(self):
        return print(f"Deleting {self.item} from the menu")

    
    def update(self, new_item=None, new_price=None):
        if new_item is not None:
            self.name = new_item
        if new_price is not None:
            self.price = new_price
        print(f"Updating {self.name} with new price {self.price}")

