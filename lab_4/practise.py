#14
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
            self.items.append(item)

class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()
    app.run(port=5001, debug=True)
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power
from datetime import datetime
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Событие: {self.type}, Данные: {self.data}"

class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage = int(damage * 0.9)  # -10%
            self._hp -= damage
        else:
            super().handle_event(event)


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)  # +10%
                self.inventory.add_item(item)
        else:
            super().handle_event(event)

class Logger:
    def log(self, event, player, filename: str):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    def read_logs(self, filename: str):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 4:
                    continue

                timestamp = parts[0]
                player_id = int(parts[1])
                event_type = parts[2]
                data = eval(parts[3])
                e = Event(event_type, data)
                e.timestamp = timestamp
                events.append(e)
                return events

class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event

    def damage_stream(events):
        for event in events:
            if event.type == "ATTACK":
                yield event.data.get("damage", 0)

    events = [
        Event("ATTACK", {"damage": 10}),
        Event("HEAL", {"heal": 5}),
        Event("ATTACK", {"damage": 20})]
    for dmg in damage_stream(events):
        print(dmg)

        def generate_events(players, items, n):
            return [Event("ATTACK", {"damage": 10}) for _ in range(n)]

def analyze_logs(events):
    total = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    players = {}
    types = {}
    for e in events:
        types[e.type] = types.get(e.type, 0) + 1
        if e.type == "ATTACK":
            pid = e.data.get("player_id", 0)
            players[pid] = players.get(pid, 0) + e.data.get("damage", 0)
    top_player = max(players, key=players.get) if players else None
    most_common = max(types, key=types.get)
    return {"total_damage": total,"top_player": top_player,"most_common_event": most_common}
class Player:
    def __init__(self, name, hp):
        self.__hp = hp
        self.__inventory = []
        self.name = name



class Warrior(Player):
    def take_damage(self, damage):
        # Уменьшает входящий урон на 10%
        reduced_damage = damage * 0.9
        return super().take_damage(reduced_damage)


class Mage(Player):
    def add_item(self, item_name, power):
        # Усиливает предмет на 10% при добавлении
        enhanced_power = power * 1.1
        return super().add_item(item_name, enhanced_power)


warrior = Warrior("Конан", 100)
mage = Mage("Гэндальф", 80)

results = []

# Тест Воина
results.append(f"--- Воин {warrior.name} ---")
results.append(warrior.take_damage(20))

# Тест Мага
results.append(f"\n--- Маг {mage.name} ---")
results.append(mage.add_item("Посох", 100))
results.append(f"Инвентарь мага: {mage.inventory}")
print("\n".join(results))

@app.route('/')
def home():
    return "Сервер работает"

@property
def hp(self):
    return self.__hp
@hp.setter
def hp(self, value):
        self.__hp = max(0, value)

@property
def inventory(self):
    return self.__inventory


def take_damage(self, damage):
    self.hp -= damage
    return f"{self.name} получил {damage} урона. HP: {self.hp}"


def add_item(self, item_name, power):
    self.__inventory.append({"name": item_name, "power": power})
    return f"Предмет {item_name} добавлен."
if __name__ == '__main__':
    app.run(port=5001, debug=True)