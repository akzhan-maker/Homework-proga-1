#1
'''
class User:
    def __init__(self, user_id, name, email):
        self._id = user_id

        self._name = name.strip().title()

        processed_email = email.lower()

        if '@' not in processed_email:
            raise ValueError("Некорректный email: отсутствует символ '@'")

        self._email = processed_email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")
try:
    u = User(1, "  john doe  ", "John@Example.COM")
    print(u
    del u

except ValueError as e:
    print(e)

#2
class User:
    def __init__(self, user_id, name, email):
        self._id = int(user_id)
        self._name = name.strip().title()
        processed_email = email.strip().lower()

        if '@' not in processed_email:
            raise ValueError("Некорректный email")
        self._email = processed_email

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')

        clean_parts = [part.strip() for part in parts]

        return cls(clean_parts[0], clean_parts[1], clean_parts[2])

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

u = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u)
#3
class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def __str__(self): п
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

p1 = Product(1, "Laptop", 1200.0, "Electronics")
p2 = Product(1, "Laptop", 1200.0, "Electronics")
p3 = Product(2, "Mouse", 25.0, "Electronics")

print(f"Словарь: {p1.to_dict()}")
product_set = {p1, p2, p3}
print(f"Количество уникальных товаров: {len(product_set)}")

#4
class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}')"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if any(p.id == product.id for p in self.products):
            return
        self.products.append(product)

    def get_all_products(self):
        return self.products

    def to_dict(self):
        return {p.id: p for p in self.products}


inv = Inventory()
p1 = Product(1, "Laptop", 1200.0, "Electronics")
p2 = Product(2, "Mouse", 25.0, "Electronics")

inv.add_product(p1)
inv.add_product(p2)

print(f"Всего товаров: {len(inv.get_all_products())}")
print(f"Словарь инвентаря: {inv.to_dict()}")
'''
