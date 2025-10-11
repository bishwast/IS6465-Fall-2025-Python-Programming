import parts_inventory as hw

parts = hw.Parts()
inventory = hw.Inventory()
# inventory.reset_database()
inventory.add_inv("Bottled Water", 24, "1.50")
# inventory.update_inv(1, 10, "1.99")
print(inventory.fetch_inv(1))
inventory.delete_inv(1)
print(inventory.fetch_inv())
