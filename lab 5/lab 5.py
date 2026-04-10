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


print("--- Задача 1 ---")
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

print("\n--- Задача 2 ---")
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

print("\n--- Задача 3 ---")
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


print("\n--- Задача 4 ---")


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

print("\n--- Задача 5 ---")
class MockProduct:
    def __init__(self, name, price): self.name = name; self.price = price

test_list = [MockProduct("Mouse", 20), MockProduct("Monitor", 300)]
filtered = filter_by_price(test_list, 100)
print(f"Товары дороже 100: {[p.name for p in filtered]}")
'''
#6