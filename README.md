# TestHomeWorkRepository

# Sport Shoes Store

Welcome to the Sport Shoes Store! This Python implementation includes classes for managing sneakers and a sports shoe store. The project consists of two classes: `Sneakers` and `SportShoesStore`. The classes are designed to handle information about individual sneakers and manage the inventory of a sports shoe store.

## Sneakers Class

The `Sneakers` class represents individual pairs of sneakers and includes the following attributes:

- **brand:** The brand of the sneakers.
- **size:** The size of the sneakers.
- **color:** The color of the sneakers.
- **price:** The price of the sneakers.
- **quantity:** The quantity of the sneakers in stock.
- **material:** The material used in the sneakers.
- **numberOfSales:** The number of sales for the sneakers.

## SportShoesStore Class

The `SportShoesStore` class manages the inventory of the sports shoe store. It includes the following methods:

### Sorting Methods

1. **Sort by Price:**
   - Method: `sort_by_price()`
   - Description: Sorts the inventory of sneakers by price in ascending order.

2. **Sort by Quantity:**
   - Method: `sort_by_quantity()`
   - Description: Sorts the inventory of sneakers by quantity in descending order.

### Top Selling Sneakers

- **Method: `top_selling_sneakers(n=5)`**
  - Description: Retrieves the top `n` best-selling sneakers based on the number of sales.

## Example Usage

```python
# Create Sneakers instances
sneakers1 = Sneakers("Nike", 10, "Red", 120.0, 50, "Leather", 100)
sneakers2 = Sneakers("Adidas", 9, "Blue", 90.0, 30, "Mesh", 80)

# Create SportShoesStore instance
store_inventory = [sneakers1, sneakers2]
shoe_store = SportShoesStore(store_inventory)

# Example usage of sorting methods
sorted_by_price = shoe_store.sort_by_price()
sorted_by_quantity = shoe_store.sort_by_quantity()

# Example usage of top selling sneakers
top_sellers = shoe_store.top_selling_sneakers(3)
