from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd
import datetime
from typing import List, Dict, Optional

app = FastAPI(title="Laboratory Work API")

class User:
    def __init__(self, user_id: int, name: str, email: str = ""):
        self.user_id = user_id
        self.name = name.strip().title()
        self.email = email.strip().lower()

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        if len(parts) < 3:
            raise ValueError("Неверный формат строки")
        return cls(int(parts[0]), parts[1], parts[2])

    def to_dict(self):
        return {"id": self.user_id, "name": self.name, "email": self.email}


class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str = ""):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def to_dict(self):
        return {"id": self.product_id, "name": self.name, "price": self.price, "category": self.category}

@app.get("/")
def read_root():
    return {"message": "Перейдите к конкретной задаче, например /task1, /task2 и т.д."}


@app.get("/task1")
def task_1():
    try:
        u = User(1, "  john doe  ", "John@Example.COM")
        return {"result": f"User(id={u.user_id}, name='{u.name}', email='{u.email}')"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/task2")
def task_2():
    u = User.from_string("2, Alice Wonderland , alice@wonder.com")
    return {"created_from_string": u.to_dict()}


@app.get("/task3")
def task_3():
    p1 = Product(1, "Laptop", 1200.0, "Tech")
    p2 = Product(1, "Laptop", 1200.0, "Tech")
    return {
        "product_dict": p1.to_dict(),
        "is_equal_by_id": p1.product_id == p2.product_id
    }


@app.get("/task4")
def task_4():
    products = []

    def add_p(p_list, new_p):
        if any(p['id'] == new_p['id'] for p in p_list):
            return "Warning: Duplicate ID"
        p_list.append(new_p)
        return "Added"

    inventory = []
    add_p(inventory, {"id": 1, "name": "Phone"})
    msg = add_p(inventory, {"id": 1, "name": "Phone"})
    return {"inventory": inventory, "last_action_msg": msg}


@app.get("/task5")
def task_5(min_price: float = 100):
    # Задача 5: Фильтрация через lambda
    test_list = [Product(1, "Mouse", 20), Product(2, "Monitor", 300)]
    filtered = [p.to_dict() for p in test_list if p.price >= min_price]
    return {"filtered_products": filtered}


@app.get("/task6")
def task_6():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"timestamp": timestamp, "user_id": 77, "action": "view_details", "product_id": 1024}
    return {"log_example": log_entry}


@app.get("/task7")
def task_7():
    customer = User(1, "Алихан")
    p1 = Product(1, "Клавиатура", 15000)
    p2 = Product(2, "Мышь", 8000)

    products = [p1.to_dict(), p2.to_dict()]
    total = sum(p['price'] for p in products)

    return {
        "customer": customer.name,
        "items": products,
        "total_price": total
    }


@app.get("/task8")
def task_8():
    prods = [
        Product(1, "Мышь", 5000),
        Product(2, "Монитор", 85000),
        Product(3, "Клавиатура", 12000)
    ]
    sorted_p = sorted(prods, key=lambda x: x.price, reverse=True)
    return {"top_2_expensive": [p.to_dict() for p in sorted_p[:2]]}


@app.get("/task9")
def task_9():
    catalog = [Product(1, "Наушники", 25000), Product(2, "Коврик", 4500)]
    prices = [price for price in (p.price for p in catalog)]
    return {"price_stream_output": prices}


@app.get("/task10")
def task_10():
    orders = [{"id": 501, "total": 12500}, {"id": 502, "total": 3400}]
    return {"iterated_orders": orders}


@app.get("/task11")
def task_11():
    prices = [1200.0, 25.0]
    price_array = np.array(prices)
    return {
        "array": price_array.tolist(),
        "dtype": str(price_array.dtype)
    }


@app.get("/task12")
def task_12():
    prices = np.array([1200.0, 25.0, 450.0])
    return {
        "mean": float(np.mean(prices)),
        "median": float(np.median(prices))
    }


@app.get("/task13")
def task_13():
    prices = np.array([1200.0, 25.0, 450.0])
    norm = (prices - np.min(prices)) / (np.max(prices) - np.min(prices))
    return {"normalized_prices": norm.tolist()}


@app.get("/task14")
def task_14():
    categories = np.array(["Electronics", "Clothing", "Tech"])
    return {"categories": categories.tolist()}


@app.get("/task15")
def task_15():
    arr = np.array(["Electronics", "Clothing", "Electronics"])
    return {"unique_count": int(np.unique(arr).size)}


@app.get("/task16")
def task_16():
    prices = np.array([1200.0, 25.0, 450.0])
    mean_val = np.mean(prices)
    expensive = [p for p in [1200.0, 25.0, 450.0] if p > mean_val]
    return {"mean": mean_val, "expensive_prices": expensive}

@app.get("/task17")
def task_17():
    prices = np.array([1200.0, 25.0, 450.0])
    discounted = prices * 0.9
    return {
        "original": prices.tolist(),
        "with_10_percent_discount": discounted.tolist()
    }

class Inventory:
    def __init__(self, items: List[Dict]):
        self.__items = items

    def __iter__(self):
        return iter(self.__items)

    def get_strong_items(self, threshold: int):
        return [item for item in self.__items if item.get('power', 0) > threshold]

    def get_all(self):
        return self.__items


class Player:
    def __init__(self, name: str, hp: int, inventory_items: List[Dict]):
        self.name = name
        self.__hp = hp
        self.__inventory = Inventory(inventory_items)
    @property
    def hp(self):
        return self.__hp

    @property
    def inventory(self):
        return self.__inventory
    def __del__(self):
        print(f"Player {self.name} удалён")


def analyze_inventory(players: List[Player]):
    all_items_names = []
    top_power_item = {"name": "None", "power": 0}

    for player in players:
        for item in player.inventory:
            name = item.get('name')
            power = item.get('power', 0)
            all_items_names.append(name)

            if power > top_power_item['power']:
                top_power_item = item

    return {
        "unique_items": list(set(all_items_names)),  # Set для уникальности
        "top_power": top_power_item
    }


@app.get("/task18_19")
def task_18_19():
    p1 = Player("Arthur", 100, [{"name": "Sword", "power": 50}, {"name": "Shield", "power": 20}])
    p2 = Player("Merlin", 80, [{"name": "Magic Wand", "power": 80}, {"name": "Potion", "power": 10}])

    analysis = analyze_inventory([p1, p2])
    return {
        "unique_equipment": analysis["unique_items"],
        "most_powerful_item": analysis["top_power"]
    }


@app.get("/task20")
def task_20():
    warrior = Player("Lancelot", 120, [{"name": "Axe", "power": 60}, {"name": "Helmet", "power": 15}])
    mage = Player("Gandalf", 70, [{"name": "Staff", "power": 90}])

    players = [warrior, mage]
    stats = analyze_inventory(players)

    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "players": [p.name for p in players],
        "results": stats
    }

    try:
        with open("game_logs.json", "w", encoding="utf-8") as f:
            import json
            json.dump(log_entry, f, ensure_ascii=False)
        log_status = "Логи успешно записаны в game_logs.json"
    except Exception:
        log_status = "Ошибка записи файла"

    return {
        "simulation_status": "Completed",
        "log_status": log_status,
        "summary": {
            "total_players": len(players),
            "max_damage_item": stats["top_power"]["name"]
        }
    }


@app.get("/task21")
def task_21():
    users_data = [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "registration_date": "2026-03-18"},
        {"id": 2, "name": "Alice", "email": "alice@example.com", "registration_date": "2026-03-18"}
    ]

    df = pd.DataFrame(users_data)

    return {
        "columns": df.columns.tolist(),
        "data": df.to_dict(orient="records")
    }


@app.get("/task22")
def task_22():
    products = [
        Product(1, "Laptop", 1200.0, "Electronics"),
        Product(2, "T-Shirt", 20.0, "Clothing")
    ]

    data = [p.to_dict() for p in products]

    df = pd.DataFrame(data)
    df = df[["id", "name", "category", "price"]]

    return {
        "status": "success",
        "columns": df.columns.tolist(),
        "data": df.to_dict(orient="records")
    }


@app.get("/task23")
def task_23():
    users_df = pd.DataFrame([
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ])
    orders_df = pd.DataFrame([
        {"order_id": 101, "user_id": 1, "total": 1200},
        {"order_id": 102, "user_id": 2, "total": 25}
    ])

    merged_df = pd.merge(
        users_df,
        orders_df,
        left_on="id",
        right_on="user_id"
    )

    result_df = merged_df[["order_id", "name", "total"]].rename(columns={"name": "user_name"})

    return {
        "description": "Объединение таблиц завершено",
        "merged_data": result_df.to_dict(orient="records")
    }


@app.get("/task24")
def task_24(min_total: float = 100.0):
    users_df = pd.DataFrame([
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ])
    orders_df = pd.DataFrame([
        {"order_id": 101, "user_id": 1, "total": 1200},
        {"order_id": 102, "user_id": 2, "total": 25}
    ])

    merged_df = pd.merge(users_df, orders_df, left_on="id", right_on="user_id")
    df = merged_df[["order_id", "name", "total"]].rename(columns={"name": "user_name"})

    filtered_df = df[df['total'] > min_total]

    return {
        "filter_applied": f"total > {min_total}",
        "result": filtered_df.to_dict(orient="records")
    }


@app.get("/task25")
def task_25():
    data = [
        {"order_id": 101, "user_name": "John", "total": 1200},
        {"order_id": 103, "user_name": "John", "total": 500},
        {"order_id": 102, "user_name": "Alice", "total": 25}
    ]
    df = pd.DataFrame(data)
    grouped_df = df.groupby("user_name")["total"].sum().reset_index()

    grouped_df = grouped_df.rename(columns={"total": "total_sum"})

    return {
        "description": "Суммарные траты пользователей рассчитаны",
        "result": grouped_df.to_dict(orient="records")
    }
@app.get("/task26")
def task_26():
    df = get_sample_df()
    result = df.groupby("user_name")["total"].mean().reset_index()
    return result.rename(columns={"total": "mean_total"}).to_dict(orient="records")

@app.get("/task27")
def task_27():
    df = get_sample_df()
    result = df.groupby("user_name")["order_id"].count().reset_index()
    return result.rename(columns={"order_id": "orders_count"}).to_dict(orient="records")


@app.get("/task28")
def task_28():
    products_data = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
        {"id": 2, "name": "Mouse", "category": "Electronics", "price": 25},
        {"id": 3, "name": "Shirt", "category": "Clothing", "price": 20}
    ]
    df = pd.DataFrame(products_data)
    result_df = df.groupby("category")["price"].mean().reset_index()
    result_df = result_df.rename(columns={"price": "mean_price"})

    return {
        "description": "Средняя цена по категориям рассчитана",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task29")
def task_29():
    data = [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Mouse", "price": 25}
    ]
    df = pd.DataFrame(data)
    df['discounted_price'] = df['price'] * 0.9

    return {
        "status": "success",
        "result": df.to_dict(orient="records")
    }


@app.get("/task30")
def task_30():
    data = [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Mouse", "price": 25},
        {"id": 3, "name": "Monitor", "price": 450}
    ]
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by="price", ascending=False)

    return {
        "status": "success",
        "result": sorted_df.to_dict(orient="records")
    }


@app.get("/task31")
def task_31():
    data = [
        {"order_id": 101, "product_name": "Laptop", "price": 1200},
        {"order_id": 102, "product_name": "Mouse", "price": 25}
    ]
    df = pd.DataFrame(data)

    df['quantity'] = 1

    return {
        "description": "Колонка quantity добавлена",
        "result": df.to_dict(orient="records")
    }


@app.get("/task32")
def task_32():
    data = [
        {"order_id": 101, "product_name": "Laptop", "price": 1200, "quantity": 1},
        {"order_id": 102, "product_name": "Mouse", "price": 25, "quantity": 2}
    ]
    df = pd.DataFrame(data)

    df['total_price'] = df['price'] * df['quantity']

    return {
        "result": df.to_dict(orient="records")
    }


@app.get("/task33")
def task_33():
    data = [
        {"product_name": "Laptop", "category": "Electronics", "price": 1200},
        {"product_name": "T-Shirt", "category": "Clothing", "price": 20}
    ]
    df = pd.DataFrame(data)

    electronics_df = df[df['category'] == "Electronics"]

    return {
        "result": electronics_df.to_dict(orient="records")
    }


@app.get("/task34")
def task_34():
    data = [
        {"product_name": "Laptop", "category": "Electronics"},
        {"product_name": "Mouse", "category": "Electronics"},
        {"product_name": "Shirt", "category": "Clothing"}
    ]
    df = pd.DataFrame(data)

    result_df = df.groupby("category")["product_name"].count().reset_index()

    result_df = result_df.rename(columns={"product_name": "count"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task35")
def task_35():
    products_data = [
        {"product_name": "Laptop", "category": "Electronics", "price": 1200},
        {"product_name": "Mouse", "category": "Electronics", "price": 25},
        {"product_name": "Shirt", "category": "Clothing", "price": 20}
    ]
    df = pd.DataFrame(products_data)

    result_df = df.groupby("category")["price"].mean().reset_index()

    result_df = result_df.rename(columns={"price": "mean_price"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task36")
def task_36():
    data = [
        {"order_id": 101, "total_price": 1200},
        {"order_id": 102, "total_price": 50}
    ]
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by="total_price", ascending=False)

    return {
        "status": "success",
        "result": sorted_df.to_dict(orient="records")
    }


@app.get("/task37")
def task_37():
    data = [
        {"order_id": 101, "total_price": 1200},
        {"order_id": 102, "total_price": 50},
        {"order_id": 103, "total_price": 500},
        {"order_id": 104, "total_price": 1500}
    ]
    df = pd.DataFrame(data)
    top_3_df = df.sort_values(by="total_price", ascending=False).head(3)

    return {
        "status": "success",
        "result": top_3_df.to_dict(orient="records")
    }


@app.get("/task38")
def task_38():
    users_data = [
        {"user_id": 1, "user_name": "John"},
        {"user_id": 2, "user_name": "Alice"}
    ]
    orders_data = [
        {"order_id": 101, "user_id": 1, "total_price": 1200},
        {"order_id": 102, "user_id": 2, "total_price": 50}
    ]

    df_users = pd.DataFrame(users_data)
    df_orders = pd.DataFrame(orders_data)

    merged_df = pd.merge(df_orders, df_users, on="user_id")

    result_df = merged_df[["order_id", "user_name", "total_price"]]

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task39")
def task_39():
    data = [
        {"user_name": "John", "total_price": 1200},
        {"user_name": "John", "total_price": 500},
        {"user_name": "Alice", "total_price": 50}
    ]
    df = pd.DataFrame(data)

    result_df = df.groupby("user_name")["total_price"].mean().reset_index()

    result_df = result_df.rename(columns={"total_price": "mean_total"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task40")
def task_40():
    data = [
        {"user_name": "John", "order_id": 101},
        {"user_name": "John", "order_id": 103},
        {"user_name": "Alice", "order_id": 102}
    ]
    df = pd.DataFrame(data)

    result_df = df.groupby("user_name")["order_id"].count().reset_index()

    result_df = result_df.rename(columns={"order_id": "orders_count"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task41")
def task_41():
    data = [
        {"user_name": "John", "total_price": 1200},
        {"user_name": "John", "total_price": 500},
        {"user_name": "Alice", "total_price": 50}
    ]
    df = pd.DataFrame(data)

    result_df = df.groupby("user_name")["total_price"].max().reset_index()

    result_df = result_df.rename(columns={"total_price": "max_order"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task42")
def task_42():
    data = [
        {"user_name": "John", "category": "Electronics"},
        {"user_name": "John", "category": "Electronics"},
        {"user_name": "John", "category": "Clothing"},
        {"user_name": "Alice", "category": "Clothing"}
    ]
    df = pd.DataFrame(data)

    result_df = df.groupby("user_name")["category"].nunique().reset_index()

    result_df = result_df.rename(columns={"category": "unique_categories"})

    return {
        "status": "success",
        "result": result_df.to_dict(orient="records")
    }


@app.get("/task43")
def task_43():
    data = [
        {"user_name": "John", "total_sum": 1700},
        {"user_name": "Alice", "total_sum": 25}
    ]
    df = pd.DataFrame(data)

    df["VIP"] = df["total_sum"] > 1000

    return {
        "status": "success",
        "result": df.to_dict(orient="records")
    }


@app.get("/task44")
def task_44():
    data = [
        {"user_name": "John", "total_sum": 1700, "mean_total": 850},
        {"user_name": "Alice", "total_sum": 25, "mean_total": 25},
        {"user_name": "Bob", "total_sum": 1700, "mean_total": 600}
    ]
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(
        by=["total_sum", "mean_total"],
        ascending=[False, True]
    )

    return {
        "status": "success",
        "result": sorted_df.to_dict(orient="records")
    }


@app.get("/task45")
def task_45():
    data = [
        {"user_name": "John", "order_id": 101, "total_price": 1200, "category": "Electronics"},
        {"user_name": "John", "order_id": 103, "total_price": 500, "category": "Clothing"},
        {"user_name": "Alice", "order_id": 102, "total_price": 25, "category": "Clothing"}
    ]
    df = pd.DataFrame(data)

    report = df.groupby("user_name").agg(
        total_orders=("order_id", "count"),
        total_sum=("total_price", "sum"),
        mean_total=("total_price", "mean"),
        max_order=("total_price", "max"),
        unique_categories=("category", "nunique")
    ).reset_index()

    report["VIP"] = report["total_sum"] > 1000

    return {
        "status": "success",
        "result": report.to_dict(orient="records")
    }