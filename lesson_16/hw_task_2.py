# Write a class Product that has three attributes:
# type
# name
# price

# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#
# Tips: Use aggregation / composition concepts while implementing the ProductStore class.You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:

#     1. add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
#
#     2. set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
#
#     3. sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
#
#     4. get_income() - returns amount of many earned by ProductStore instance.

#     5. get_all_products() - returns information about all available products in the store.
#
#     6. get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, name, price, distributor):
        self.name = name
        self.price = price
        self.distributor = distributor

    def __str__(self):
        return f"{self.name} ({self.distributor}) - {self.price}$"




class ProductInStore(Product):
    store_price_factor = 1.3

    def __init__(self, name, price, distributor):
        super().__init__(name, price, distributor)
        self.price *= self.store_price_factor


class ProductStore:
    def __init__(self):
        self.products = {}
        self.products_list = []
        self.income = 0
        self.balance = 0

    def add(self, product: Product, amount: int):
        product_in_store = ProductInStore(**product.__dict__)

        self.products[product_in_store.name] = {
            "product": product_in_store,
            "amount": amount,
        }

        self.balance -= product.price * amount

    def sell_product(self, name: str, amount: int):
        product_data = self.products.get(name)
        if product_data is None:
            raise ValueError(f"No such product: {name}")

        if product_data["amount"] < amount:
            raise ValueError(f"Not enough products (we have {product_data['amount']}, you asking {amount})")

        self.balance += product_data["product"].price * product_data["amount"]
        self.products[name]["amount"] -= amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        discount_factor = (100 - percent) / 100
        if identifier_type == "name":
            product_data = self.products.get(identifier)
            if product_data is None:
                raise ValueError(f"No such product: {identifier}")

            self.products[identifier]["product"].price *= discount_factor

        if identifier_type == "type":
            for product_name, product_data in self.products.items():
                if isinstance(product_data["product"], identifier):
                    self.products[product_name]["product"].price *= discount_factor

    def get_balance(self):
        print(self.balance, "$")

    def get_products(self):
        for product_name, product_data in self.products.items():
            print(product_data["product"])



milk = Product("Milk", 10, "PepsiCo")
orange = Product("Orange", 100, "Farm")

store = ProductStore()


store.add(milk, 20)
store.add(orange, 1000)

store.get_products()
store.get_balance()


store.set_discount("Milk", 30, "name" )
store.set_discount("Orange", 30, "name" )

store.sell_product("Milk", 20)
store.sell_product("Orange", 1000)

print("--------------------")
store.get_products()
store.get_balance()




