class Item:
    """Class to represent an item with name, price, and quantity."""
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculate total price for the item."""
        return self.price * self.quantity


class Cashier:
    """Class to represent a cashier that handles transactions."""
    def __init__(self):
        self.cart = []

    def add_item(self, item: Item):
        """Add an item to the cart."""
        self.cart.append(item)
    
    def calculate_total(self) -> float:
        """Calculate total cost for all items in the cart."""
        total = sum(item.total_price() for item in self.cart)
        return total

    def print_receipt(self):
        """Print the receipt with all items and total cost."""
        print("---- Receipt ----")
        for item in self.cart:
            print(f"{item.name} x{item.quantity} - ${item.total_price():.2f}")
        print("-----------------")
        print(f"Total: ${self.calculate_total():.2f}")
        

# Example usage:
if __name__ == "__main__":
    cashier = Cashier()
    
    item1 = Item("Apple", 0.50, 4)   # 4 Apples at $0.50 each
    item2 = Item("Bread", 2.00, 1)   # 1 Bread at $2.00 each
    item3 = Item("Milk", 1.50, 2)    # 2 Milk at $1.50 each
    
    cashier.add_item(item1)
    cashier.add_item(item2)
    cashier.add_item(item3)
    
    cashier.print_receipt()
