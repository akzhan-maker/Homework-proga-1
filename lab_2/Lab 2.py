#ex 1
users = set()
buy_count = 0
total_sum = 0
user_spend = {}

with open("shop_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        print(parts)
        date = parts[0]
        user = parts[1]
        action = parts[2]

        users.add(user)

        if action == "BUY":
            amount = int(parts[3]) #amount- сумма, parts[3] сумма покупок, строка --> число
            buy_count += 1
            total_sum += amount

            if user not in user_spend:
                user_spend[user] = amount
            else:
                user_spend[user] += amount
max_user = None
max_sum = 0

for user in user_spend:
    if user_spend[user] > max_sum:
        max_sum = user_spend[user]
        max_user = user
if buy_count != 0:
    avg_check = total_sum / buy_count
else:
    avg_check = 0
with open("report.txt", "w", encoding="utf-8") as r:
    r.write(f"Қолданушылар саны: {len(users)}\n")
    r.write(f"Барлық сатылымдар саны: {buy_count}\n")
    r.write(f"Жалпы сумма: {total_sum}\n")
    r.write(f"Ең активный пайдаланушы: {max_user}\n")
    r.write(f"Средний чек: {avg_check}\n")
print("Отчет құрылды: report.txt")
with open("report.txt", "r", encoding="utf-8") as f:
     print(f.read())



#ex2
import csv

employees = []
try:
    with open('employees.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['salary'] = int(row['salary'])
            employees.append(row)
except FileNotFoundError:
    print("Файл employees.csv не найден!")
    exit()

total_salary = sum(emp['salary'] for emp in employees)
avg_salary = total_salary / len(employees)

dept_data = {}
for emp in employees:
    dept = emp['department']
    if dept not in dept_data:
        dept_data[dept] = []
    dept_data[dept].append(emp['salary'])

avg_per_dept = {dept: sum(salaries)/len(salaries) for dept, salaries in dept_data.items()}

best_dept = max(avg_per_dept, key=avg_per_dept.get)
richest_employee = max(employees, key=lambda x: x['salary'])

high_earners = [emp for emp in employees if emp['salary'] > avg_salary]

with open('high_salary.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'department', 'salary'])
    writer.writeheader()
    writer.writerows(high_earners)

print(f"Средняя зарплата: {avg_salary:.2f}")
print("Средняя зарплата по отделам:")
for dept, val in avg_per_dept.items():
    print(f"  - {dept}: {val:.2f}")
print(f"Отдел с самой высокой средней зарплатой: {best_dept}")
print(f"Самый высокооплачиваемый сотрудник: {richest_employee['name']} ({richest_employee['salary']})")
print("\nСотрудники выше среднего (сохранены в high_salary.csv):")
for emp in high_earners:
    print(f"  - {emp['name']}: {emp['salary']}")



#ex3
import json

with open('orders.json', 'r', encoding='utf-8') as f:
    orders = json.load(f)

total_revenue = sum(order['total'] for order in orders)

user_orders_count = {}
all_items = []

for order in orders:
    user = order['user']
    user_orders_count[user] = user_orders_count.get(user, 0) + 1

    all_items.extend(order['items'])

total_items_sold = len(all_items)


top_order = max(orders, key=lambda x: x['total'])
top_user = top_order['user']

item_frequency = {}
for item in all_items:
    item_frequency[item] = item_frequency.get(item, 0) + 1

most_popular_item = max(item_frequency, key=item_frequency.get)


summary = {
    "total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=4, ensure_ascii=False)

print(f"Общая сумма: {total_revenue}")
print(f"Кол-во товаров: {total_items_sold}")
print(f"Топ пользователь: {top_user}")
print(f"Популярный товар: {most_popular_item}")
print("\nЗаказы по пользователям:")
for user, count in user_orders_count.items():
    print(f" - {user}: {count}")



#ex4
import csv
import json

transactions = []
user_op_counts = {}

with open('transactions.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['amount'] = int(row['amount'])
        transactions.append(row)
        uid = row['user_id']
        user_op_counts[uid] = user_op_counts.get(uid, 0) + 1

suspicious_transactions = [t for t in transactions if t['amount'] > 500000]
suspicious_users = [uid for uid, count in user_op_counts.items() if count > 3]

total_suspicious_amount = sum(t['amount'] for t in suspicious_transactions)

with open('fraud_report.txt', mode='w', encoding='utf-8') as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users) if suspicious_users else 'Нет'}\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")

with open('fraud_users.json', mode='w', encoding='utf-8') as f:
    json.dump({"fraud_users": suspicious_users}, f, indent=4)

print("Анализ завершен. Файлы fraud_report.txt и fraud_users.json созданы.")