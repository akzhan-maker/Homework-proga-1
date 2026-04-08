
import csv
import json

transactions = []
user_op_counts = {}

with open('transactions2.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['amount'] = int(row['amount'])
        transactions.append(row)
        uid = row['user_id']
        user_op_counts[uid] = user_op_counts.get(uid, 0) + 1

suspicious_transactions = [t for t in transactions if t['amount'] > 500000]
suspicious_users = [uid for uid, count in user_op_counts.items() if count > 3]

total_suspicious_amount = sum(t['amount'] for t in suspicious_transactions)

with open('fraud_report2.txt', mode='w', encoding='utf-8') as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users) if suspicious_users else 'Нет'}\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")

with open('fraud_users2.json', mode='w', encoding='utf-8') as f:
    json.dump({"fraud_users": suspicious_users}, f, indent=4)

print("Анализ завершен. Файлы fraud_report.txt и fraud_users.json созданы.")