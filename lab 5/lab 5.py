'''
#1
class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name.strip().title()
        processed_email = email.strip().lower()

        if '@' not in processed_email:
            raise ValueError("Ошибка: в email должен быть символ @")
        self._email = processed_email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")


print(" Task 1 ")
u = User(1, "  john doe  ", "John@Example.COM")
print(f"Результат: {u}")

#2
class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name.strip().title()
        self._email = email.strip().lower()

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        return cls(int(parts[0]), parts[1], parts[2])

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

print("\n Task 2 ")
u_from_str = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(f"Создано из строки: {u_from_str}")

#3
class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "category": self.category}

    def __str__(self):
        return f"Product: {self.name} ({self.price}$)"

print("\n Task 3 ")
p1 = Product(1, "Laptop", 1200.0, "Tech")
p2 = Product(1, "Laptop", 1200.0, "Tech")
print(f"Словарь продукта: {p1.to_dict()}")
print(f"p1 == p2 (дубликаты по ID): {p1 == p2}")

#4
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if any(p.id == product.id for p in self.products):
            print(f"Предупреждение: Товар с ID {product.id} уже в списке!")
            return
        self.products.append(product)

    def to_dict(self):
        return {p.id: p.name for p in self.products}


print("\n Task 4 ")


class SimpleP:
    def __init__(self, i, n): self.id = i; self.name = n


inv = Inventory()
inv.add_product(SimpleP(1, "Phone"))
inv.add_product(SimpleP(1, "Phone"))
print(f"Содержимое инвентаря: {inv.to_dict()}")


#5
def filter_by_price(products_list, min_price):
    is_expensive = lambda p: p.price >= min_price
    return [p for p in products_list if is_expensive(p)]

print("\n Task 5 ")
class MockProduct:
    def __init__(self, name, price): self.name = name; self.price = price

test_list = [MockProduct("Mouse", 20), MockProduct("Monitor", 300)]
filtered = filter_by_price(test_list, 100)
print(f"Товары дороже 100: {[p.name for p in filtered]}")

#6
import datetime


class User:
    def __init__(self, user_id):
        self.user_id = user_id


class Product:
    def __init__(self, product_id):
        self.product_id = product_id


class Logger:
    @staticmethod
    def log_action(user: User, action: str, product: Product, filename: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp};{user.user_id};{action};{product.product_id}\n"

        with open(filename, "a", encoding="utf-8") as file:
            file.write(log_entry)

    @staticmethod
    def read_logs(filename: str) -> list:
        logs = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        logs.append({
                            'timestamp': parts[0],
                            'user_id': parts[1],
                            'action': parts[2],
                            'product_id': parts[3]
                        })
        except FileNotFoundError:
            pass
        return logs


user = User(user_id=77)
prod = Product(product_id=1024)
file_name = "logs.txt"
Logger.log_action(user, "view_details", prod, file_name)
Logger.log_action(user, "add_to_cart", prod, file_name)

print("Task 6 Содержимое лог-файла (в виде словарей) ")
log_data = Logger.read_logs(file_name)
for entry in log_data:
    print(entry)

#7
class User:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id: int, user: User, products: list = None):
        self.id = order_id
        self.user = user
        self.products = products if products is not None else []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.product_id != product_id]

    def total_price(self) -> float:
        return sum(p.price for p in self.products)

    def __str__(self):
        item_names = ", ".join([p.name for p in self.products])
        return (f"Заказ #{self.id} | Клиент: {self.user.name}\n"
                f"Товары: {item_names if item_names else 'Пусто'}\n"
                f"Итоговая сумма: {self.total_price()} тенге")

customer = User("Алихан")
p1 = Product(1, "Клавиатура", 15000)
p2 = Product(2, "Мышь", 8000)

my_order = Order(101, customer)

print("Task 7 Добавление товаров ")
my_order.add_product(p1)
my_order.add_product(p2)
print(my_order)

print("\nУдаление товара (ID: 2)")
my_order.remove_product(2)
print(my_order)

#8
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.price} тг)"


class Order:
    def __init__(self, products: list):
        self.products = products

    def most_expensive_products(self, n: int) -> list:
        sorted_products = sorted(self.products, key=lambda p: p.price, reverse=True)
        return sorted_products[:n]


prods = [
    Product("Мышь", 5000),
    Product("Монитор", 85000),
    Product("Клавиатура", 12000),
    Product("USB-хаб", 3000)
]
my_order = Order(prods)

print(" Task 8")
top_products = my_order.most_expensive_products(2)
for p in top_products:
    print(p)

#9
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def price_stream(products: list):
    for product in products:
        yield product.price

catalog = [
    Product("Наушники", 25000),
    Product("Коврик", 4500),
    Product("Веб-камера", 18000)
]

print(" Task 9")
gen = price_stream(catalog)

for price in gen:
    print(f"Цена следующего товара: {price} тг")

#10
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def __str__(self):
        return f"Заказ #{self.order_id} на сумму {self.total} тг"

class OrderIterator:
    def __init__(self, orders: list):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            return order
        else:
            raise StopIteration

orders_list = [
    Order(501, 12500),
    Order(502, 3400),
    Order(503, 8900)
]

iterator = OrderIterator(orders_list)

print(" Task 10")
for order in iterator:
    print(order)

print("\n  ")
new_iterator = OrderIterator([Order(999, 100)])
print(next(new_iterator))

#11
import numpy as np


class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.category = category


def create_price_array(products: list):
    prices = [p.price for p in products]

    return np.array(prices, dtype=float)

products = [
    Product(1, "Laptop", 1200.0, "Electronics"),
    Product(2, "Mouse", 25.0, "Electronics")
]
price_array = create_price_array(products)

print(" Task 11")
print(price_array)

print("\n data")
print(type(price_array))
print(f"Тип элементов внутри: {price_array.dtype}")

#12
import numpy as np


def calculate_stats(price_array):
    mean_price = np.mean(price_array)

    median_price = np.median(price_array)

    return (mean_price, median_price)


prices = np.array([1200.0, 25.0, 450.0])

stats = calculate_stats(prices)

print(f" result: ({round(stats[0], 2)}, {stats[1]})")

#13
import numpy as np


def normalize_prices(prices):
    min_val = np.min(prices)
    max_val = np.max(prices)

    normalized = (prices - min_val) / (max_val - min_val)

    return normalized

prices = np.array([1200.0, 25.0, 450.0])

norm_prices = normalize_prices(prices) 
print(f" result: {np.round(norm_prices, 4)}")

#14
import numpy as np


class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category


def create_category_array(products: list):

    categories = [p.category for p in products]

    return np.array(categories)

products_list = [
    Product(1, "Laptop", 1200.0, "Electronics"),
    Product(2, "T-Shirt", 20.0, "Clothing")
]
category_array = create_category_array(products_list)

print("Task 14")
print(category_array)

#15
import numpy as np


def count_unique_categories_np(category_array):
    unique_elements = np.unique(category_array)

    return unique_elements.size

input_array = np.array(["Electronics", "Clothing", "Electronics"])

result = count_unique_categories_np(input_array)

print( result )

#16
import numpy as np


class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def __repr__(self):
        return f"Product({self.product_id}, '{self.name}', {self.price}, '{self.category}')"


def get_expensive_products(products_list, price_array):

    mean_price = np.mean(price_array)

    expensive_items = [p for p in products_list if p.price > mean_price]

    return expensive_items


products = [
    Product(1, "Laptop", 1200.0, "Electronics"),
    Product(2, "Mouse", 25.0, "Electronics"),
    Product(3, "Monitor", 450.0, "Electronics")
]

prices = np.array([p.price for p in products])

result = get_expensive_products(products, prices)

print(f"price: {np.mean(prices):.2f}")
print(result)

#17
import numpy as np


def apply_discount(price_array):
    new_prices = price_array * 0.9

    return new_prices

prices = np.array([1200.0, 25.0, 450.0])

discounted_prices = apply_discount(prices)

print(f" : {prices}")
print(f" +10%: {discounted_prices}")
'''