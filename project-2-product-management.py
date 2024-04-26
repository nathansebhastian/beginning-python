import csv

PRODUCTS_FILE = "products.csv"
HEADERS = ["Name", "Price", "Stock"]

def load_products():
    try:
        with open(PRODUCTS_FILE, "r") as csvfile:
            reader = csv.reader(csvfile)
            products = list(reader)[1:]
    except FileNotFoundError:
        products = []
    return products

def view_products(products):
    print(", ".join(HEADERS))
    for product in products:
        print(", ".join(product))

def add_product(products):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    stock = input("Enter product stock: ")
    products.append([name, price, stock])
    save_products(products)
   
def save_products(products):
    with open(PRODUCTS_FILE, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(HEADERS)
        writer.writerows(products)

def remove_product(products):
    name = input("Enter product name to remove: ")
    for product in products:
        if product[0] == name:
            products.remove(product)
            save_products(products)
            print(f"{name} removed from products list.")
            return
    print(f"{name} not found in products list.")

products = load_products()
while True:
    print("\nOptions:")
    print("1. View products")
    print("2. Add product")
    print("3. Remove product")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_products(products)
    elif choice == "2":
        add_product(products)
    elif choice == "3":
        remove_product(products)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")