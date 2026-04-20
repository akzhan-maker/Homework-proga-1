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
