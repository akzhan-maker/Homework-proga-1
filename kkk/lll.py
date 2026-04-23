'''
#17
import pandas as pd

try:
    df = pd.read_excel('catalog_analysis.xlsx')
except FileNotFoundError:
    df = pd.read_excel('catalog_products.xlsx')
    df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
    df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

df['total_value'] = df['col_2'] * df['col_3']

top_10_stocks = df.sort_values(by='total_value', ascending=False).head(10)

result = top_10_stocks[['col_1', 'col_2', 'col_3', 'total_value']]

print("--- Задача 17: Топ-10 товаров по суммарной стоимости на складе ---")
print(result)

result.to_excel('top_10_inventory_value.xlsx', index=False)
'''

#18
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
try:
    df = pd.read_excel('catalog_analysis.xlsx')
except FileNotFoundError:
    df = pd.read_excel('catalog_products.xlsx')

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['до 50', '50-200', '200-500', '500-1000', 'больше 1000']

df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)

price_dist = df['price_range'].value_counts().reindex(labels).reset_index()
price_dist.columns = ['price_range', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=price_dist, x='price_range', y='count', palette='magma')

plt.title('Задача 18: Распределение товаров по ценовым диапазонам')
plt.xlabel('Ценовой диапазон')
plt.ylabel('Количество товаров')

for i, val in enumerate(price_dist['count']):
    plt.text(i, val + 0.5, int(val), ha='center')

plt.show()
print("--- Задача 18: Распределение цен ---")
print(price_dist)
