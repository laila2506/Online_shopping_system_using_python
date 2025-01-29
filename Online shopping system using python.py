# List of available products (ID, Name, Price)
products = {
    1: {"name": "Laptop", "price": 800},
    2: {"name": "Smartphone", "price": 400},
    3: {"name": "Headphones", "price": 50},
    4: {"name": "Keyboard", "price": 25}
}

# Cart to store selected items
cart = []

# Function to display products
def show_products():
    print("\nAvailable Products:")
    for product_id, product in products.items():
        print(f"{product_id}. {product['name']} - ${product['price']}")

# Function to add items to cart
def add_to_cart(product_id, quantity):
    if product_id in products:
        cart.append({"name": products[product_id]["name"], "quantity": quantity, "price": products[product_id]["price"]})
        print(f"{quantity} x {products[product_id]['name']} added to your cart!")
    else:
        print("Invalid product ID!")

# Function to view cart and checkout
def checkout():
    if cart:
        print("\nYour Cart:")
        total = 0
        for item in cart:
            print(f"{item['quantity']} x {item['name']} - ${item['price'] * item['quantity']}")
            total += item['price'] * item['quantity']
        print(f"Total: ${total}")
        print("\nThank you for shopping with us!")
    else:
        print("Your cart is empty!")

# Main function to interact with the user
def main():
    while True:
        show_products()
        choice = input("\nEnter the product ID to add to your cart (or type 'exit' to quit): ")
        
        if choice == 'exit':
            break

        try:
            product_id = int(choice)
            quantity = int(input(f"How many of {products[product_id]['name']} would you like to buy? "))
            add_to_cart(product_id, quantity)
        except ValueError:
            print("Please enter valid numbers.")

        another = input("Do you want to add more items? (yes/no): ").lower()
        if another != 'yes':
            break
    
    checkout()

if __name__ == "__main__":
    main()
