from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item):
        print(f"Retrieved item by name: {item}")
        return None

    @classmethod
    def all_items(cls):
        print("Retrieved all items from Menu_Items table")
        return []

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()
