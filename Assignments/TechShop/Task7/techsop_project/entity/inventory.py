# Inventory.Py - Placeholder
class Inventory:
    def __init__(self, inventory_id, product_id, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product_id = product_id
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    def __str__(self):
        return f"Inventory #{self.inventory_id} - Product #{self.product_id}: {self.quantity_in_stock} in stock"
