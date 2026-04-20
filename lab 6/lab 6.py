'''
#1
import pandas as pd

file_name = 'catalog_products.xlsx'

try:
    df = pd.read_excel(file_name)

    print(f"Форма DataFrame: {df.shape}")
    print("-" * 30)

    print("Типы данных:")
    print(df.dtypes)
    print("-" * 30)

    print("Пропуски в колонках:")
    print(df.isnull().sum())
    print("-" * 30)

    print("Первые 5 строк таблицы:")
    print(df.head())

except FileNotFoundError:
    print(f"Ошибка: Файл '{file_name}' не найден в папке со скриптом.")
except Exception as e:
    print(f"Произошла ошибка: {e}")


#2
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

numeric_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']

print("--- Задача 2: Приведение типов и заполнение пропусков ---")

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)

    mean_value = df[col].mean()
    df[col] = df[col].fillna(mean_value)

print("Количество пропусков после обработки:")
print(df[numeric_cols].isnull().sum())

print("\nТипы данных после преобразования:")
print(df[numeric_cols].dtypes)

print("\nПервые 5 строк (числовые данные):")
print(df[numeric_cols].head())


#3
import pandas as pd
import numpy as np

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

cols_to_fix = ['col_2', 'col_3', 'col_4']
for col in cols_to_fix:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

print("--- Задача 3: Создание новых показателей ---")

df['total_value'] = df['col_2'] * df['col_3']

df['double_stock'] = df['col_4'] * 2

df['log_price'] = np.log(df['col_2'].replace(0, 1))

print("Результат создания новых колонок (первые 5 строк):")
print(df[['col_2', 'col_3', 'col_4', 'total_value', 'double_stock', 'log_price']].head())

#4
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

print("--- Задача 4: Выбор дорогих товаров Electronics ---")

electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == "Electronics")].copy()

print(f"Найдено подходящих товаров: {len(electronics_expensive)}")
print("\nПервые 5 строк отфильтрованных данных:")
print(electronics_expensive.head())

#5
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce') # цена
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce') # количество

print("--- Задача 5: Группировка по категориям ---")

category_stats = df.groupby('col_7').agg({
    'col_2': ['mean', 'max'],
    'col_3': 'sum'
})

category_stats.columns = ['mean_price', 'max_price', 'total_quantity']
category_stats = category_stats.reset_index()
category_stats = category_stats.rename(columns={'col_7': 'category'})

print("Итоговая статистика по категориям:")
print(category_stats)

print("\nКолонки новой таблицы:", category_stats.columns.tolist())

#6
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

target_cols = [f'col_{i}' for i in range(2, 12)]
for col in target_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("--- Задача 6: Суммарная статистика ---")

stats_data = {
    'column': target_cols,
    'mean': [df[col].mean() for col in target_cols],
    'median': [df[col].median() for col in target_cols],
    'std': [df[col].std() for col in target_cols]
}

summary_df = pd.DataFrame(stats_data)

print("Сводная таблица статистик:")
print(summary_df)

print(f"\nРазмерность итоговой таблицы: {summary_df.shape}")

#7
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

print("--- Задача 7: Выявление аномальных товаров ---")

mean_price = df['col_2'].mean()
std_price = df['col_2'].std()

upper_limit = mean_price + 3 * std_price

print(f"Средняя цена: {mean_price:.2f}")
print(f"Стандартное отклонение: {std_price:.2f}")
print(f"Порог для аномалий: {upper_limit:.2f}")
print("-" * 30)

anomalies = df[df['col_2'] > upper_limit].copy()

print(f"Найдено аномально дорогих товаров: {len(anomalies)}")
if not anomalies.empty:
    print("\nПервые 5 аномальных товаров:")
    print(anomalies[['col_1', 'col_2', 'col_7']].head())
else:
    print("\nТовары с аномально высокой ценой не обнаружены.")

#8
import pandas as pd

file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)

target_cols = [f'col_{i}' for i in range(2, 12)]

for col in target_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("--- Задача 8: Корреляция числовых колонок ---")

correlation_matrix = df[target_cols].corr()

print("Фрагмент корреляционной матрицы:")
print(correlation_matrix.iloc[:5, :5])

#9
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_products.xlsx')
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

plt.figure(figsize=(10, 6))
plt.hist(df['col_2'].dropna(), bins=50, color='skyblue', edgecolor='black')

plt.title('Распределение цен товаров')
plt.xlabel('Цена товаров (col_2)')
plt.ylabel('Количество товаров')
plt.grid(axis='y', alpha=0.75)

plt.show()
#pip install matplotlib seaborn

#10
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'catalog_products.xlsx'
df = pd.read_excel(file_path)

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

plt.figure(figsize=(10, 6))

sns.regplot(x='col_2', y='col_3', data=df,
            scatter_kws={'alpha':0.5, 'color':'blue'},
            line_kws={'color':'red'})

plt.title('Взаимосвязь цены и количества товара на складе (Задача 10)')
plt.xlabel('Цена (col_2)')
plt.ylabel('Количество на складе (col_3)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

#11
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_products.xlsx')
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce') # Цена

plt.figure(figsize=(12, 6))
sns.boxplot(x='col_7', y='col_2', data=df)

plt.title('Задача 11: Распределение цен по категориям')
plt.xlabel('Категория (col_7)')
plt.ylabel('Цена (col_2)')
plt.xticks(rotation=45)
plt.show()

#12
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_products.xlsx')

selected_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']
df_plot = df[selected_cols].copy()

for col in ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']:
    df_plot[col] = pd.to_numeric(df_plot[col], errors='coerce')

df_plot = df_plot.fillna(0)

print("Генерирую парные диаграммы... Пожалуйста, подождите.")

plt.figure(figsize=(12, 10))
g = sns.pairplot(df_plot, hue='col_7', palette='bright', diag_kind='hist', corner=True)

g.fig.suptitle('Задача 12: Анализ взаимосвязей характеристик товаров', y=1.02)
plt.show()

#13
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_products.xlsx')

cols_numeric = [f'col_{i}' for i in range(2, 12)]

for col in cols_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df_numeric = df[cols_numeric].fillna(0)

plt.figure(figsize=(12, 8))

corr_matrix = df_numeric.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Задача 13: Тепловая карта корреляции числовых показателей')
plt.xlabel('Характеристики')
plt.ylabel('Характеристики')

plt.show()

#14
import pandas as pd
import numpy as np

df = pd.read_excel('catalog_products.xlsx')

for i in range(2, 5):
    col_name = f'col_{i}'
    df[col_name] = pd.to_numeric(df[col_name], errors='coerce')

df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log1p(df['col_2'])

original_cols = [f'col_{i}' for i in range(1, 12)]
new_metrics = ['total_value', 'double_stock', 'log_price']
final_df = df[original_cols + new_metrics]

output_name = 'catalog_analysis.xlsx'
final_df.to_excel(output_name, index=False)

print(f"Задача 14 выполнена! Файл '{output_name}' успешно сохранен.")

#15
import pandas as pd
import numpy as np

df = pd.read_excel('catalog_analysis.xlsx')

category_summary = df.groupby('col_7').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()

category_summary.rename(columns={'col_7': 'category'}, inplace=True)

print("--- Задача 15: Финальный агрегированный отчет ---")
print(category_summary.head())

category_summary.to_excel('category_summary_report.xlsx', index=False)
print("\nОтчет сохранен в файл 'category_summary_report.xlsx'")

#16
import pandas as pd

df = pd.read_excel('catalog_analysis.xlsx')

most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax()]

most_expensive_report = most_expensive[['col_1', 'col_2', 'col_7']]

print("--- Задача 16: Самые дорогие товары по категориям ---")
print(most_expensive_report)

most_expensive_report.to_excel('most_expensive_products.xlsx', index=False)

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

#18
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

#19
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

category_value = df.groupby('col_7').apply(
    lambda x: (x['col_2'] * x['col_3']).sum()
).reset_index()

category_value.columns = ['category', 'total_stock_value']

max_category = category_value.loc[category_value['total_stock_value'].idxmax()]

plt.figure(figsize=(12, 6))
sns.barplot(data=category_value.sort_values('total_stock_value', ascending=False),
            x='category', y='total_stock_value', palette='viridis')

plt.title('Задача 19: Суммарная стоимость товаров на складе по категориям')
plt.xlabel('Категория')
plt.ylabel('Суммарная стоимость')
plt.xticks(rotation=45)
plt.show()

print("--- Задача 19: Анализ стоимости по категориям ---")
print(category_value)
print(f"\nКатегория с наибольшим капиталом: {max_category['category']} "
      f"({max_category['total_stock_value']:.2f})")

#20
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

category_stats = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_quantity=('col_3', 'mean')
).reset_index()

category_stats.rename(columns={'col_7': 'category'}, inplace=True)

plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    data=category_stats,
    x='mean_price',
    y='mean_quantity',
    hue='category',
    s=200,
    palette='viridis'
)

for i in range(category_stats.shape[0]):
    plt.text(
        category_stats.mean_price[i] + 5,
        category_stats.mean_quantity[i],
        category_stats.category[i],
        fontsize=10
    )

plt.title('Задача 20: Средняя цена vs Средний запас по категориям')
plt.xlabel('Средняя цена')
plt.ylabel('Средний запас')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("--- Задача 20: Статистика по категориям ---")
print(category_stats)

#21
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

std_price_df = df.groupby('col_7')['col_2'].std().reset_index()
std_price_df.columns = ['category', 'std_price']

plt.figure(figsize=(10, 6))
sns.barplot(data=std_price_df.sort_values('std_price', ascending=False),
            x='std_price', y='category', palette='coolwarm')

plt.title('Задача 21: Стандартное отклонение цен по категориям')
plt.xlabel('Стандартное отклонение (разброс цен)')
plt.ylabel('Категория')
plt.show()

print("--- Задача 21: Категории с наибольшим разбросом цен ---")
print(std_price_df)

#22
import pandas as pd

try:
    df = pd.read_excel('catalog_analysis.xlsx')
except FileNotFoundError:
    df = pd.read_excel('catalog_products.xlsx')

df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

out_of_stock = df[df['col_3'] == 0]

report_columns = ['col_1', 'col_7', 'col_2']
out_of_stock_top10 = out_of_stock[report_columns].head(10)

print("--- Задача 22: Товары, которых нет на складе (первые 10) ---")
if out_of_stock_top10.empty:
    print("На складе нет товаров с нулевым запасом.")
else:
    print(out_of_stock_top10)
out_of_stock.to_excel('out_of_stock_report.xlsx', index=False)
print(f"\nПолный список (строк: {len(out_of_stock)}) сохранен в 'out_of_stock_report.xlsx'")

#23
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

category_counts = df.groupby('col_7')['col_1'].count().reset_index()
category_counts.columns = ['category', 'count']

top_5_categories = category_counts.sort_values(by='count', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_categories, x='category', y='count', palette='plasma')

plt.title('Задача 23: Топ-5 категорий по количеству наименований товаров')
plt.xlabel('Категория')
plt.ylabel('Количество товаров')

for i, val in enumerate(top_5_categories['count']):
    plt.text(i, val + (val * 0.01), int(val), ha='center', fontweight='bold')

plt.show()

print("--- Задача 23: Топ-5 категорий по количеству товаров ---")
print(top_5_categories)

#24
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

top_10_stock = df.sort_values(by='col_3', ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(data=top_10_stock, x='col_3', y='col_1', palette='viridis')

plt.title('Задача 24: Топ-10 товаров по количеству на складе')
plt.xlabel('Количество на складе')
plt.ylabel('Название товара')

for i, val in enumerate(top_10_stock['col_3']):
    plt.text(val + 1, i, int(val), va='center', fontweight='bold')

plt.show()

print("--- Задача 24: Топ-10 товаров по запасам ---")
print(top_10_stock[['col_1', 'col_3']])

#25
import pandas as pd

df = pd.read_excel('catalog_analysis.xlsx')

for col in ['col_2', 'col_3', 'total_value']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

final_report = df.groupby('col_7').agg(
    total_items=('col_1', 'count'),
    avg_price=('col_2', 'mean'),
    stock_sum=('col_3', 'sum'),
    inventory_value=('total_value', 'sum'),
    price_std=('col_2', 'std')
).reset_index()

final_report = final_report.round(2)

print("--- Задача 25: Финальный сводный отчет ---")
print(final_report)

final_report.to_excel('final_summary_report.xlsx', index=False)
print("\nЛабораторная работа завершена. Итоговый отчет сохранен в 'final_summary_report.xlsx'")

#36
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')
category_comparison = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_quantity=('col_3', 'mean')
).reset_index()

plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=category_comparison,
    x='mean_price',
    y='mean_quantity',
    hue='col_7',
    s=150,
    palette='Set1'
)
for i in range(category_comparison.shape[0]):
    plt.text(
        category_comparison.mean_price[i] + 2,
        category_comparison.mean_quantity[i],
        category_comparison.col_7[i],
        fontsize=9
    )
plt.title('Задача 36: Сравнение категорий (Средняя цена vs Средний запас)')
plt.xlabel('Средняя цена (mean_price)')
plt.ylabel('Средний запас (mean_quantity)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Категории')
plt.tight_layout()

plt.show()

print("--- Результаты Задачи 36 ---")
print(category_comparison.round(2))

#37
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

std_price_analysis = df.groupby('col_7')['col_2'].std().reset_index()
std_price_analysis.columns = ['category', 'std_price']

plt.figure(figsize=(10, 8))
sns.barplot(
    data=std_price_analysis.sort_values('std_price', ascending=False),
    x='std_price',
    y='category',
    palette='coolwarm'
)

plt.title('Задача 37: Категории с наибольшим разбросом цен (Standard Deviation)')
plt.xlabel('Стандартное отклонение цены')
plt.ylabel('Категория')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()

print("--- Результаты Задачи 37: Разброс цен ---")
print(std_price_analysis.sort_values('std_price', ascending=False))

#38
import pandas as pd

df = pd.read_excel('catalog_analysis.xlsx')

df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

out_of_stock_38 = df[df['col_3'] == 0]
report_38 = out_of_stock_38[['col_1', 'col_7', 'col_2']].head(10)

print("--- Результаты Задачи 38: Товары без запаса (Топ-10) ---")
if report_38.empty:
    print("На складе нет товаров с нулевым запасом.")
else:
    print(report_38)

out_of_stock_38.to_excel('shortage_report_task38.xlsx', index=False)

#39
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')
category_counts = df.groupby('col_7')['col_1'].count().reset_index()
category_counts.columns = ['category', 'count']

top_5_categories = category_counts.sort_values(by='count', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_categories, x='category', y='count', palette='plasma')

plt.title('Задача 39: Топ-5 категорий по наполнению ассортимента')
plt.xlabel('Категория (col_7)')
plt.ylabel('Количество наименований')

for i, val in enumerate(top_5_categories['count']):
    plt.text(i, val + 1, int(val), ha='center', fontweight='bold')

plt.show()
print("--- Результат Задачи 39 ---")
print(top_5_categories)

#40
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

top_10_stock = df.sort_values(by='col_3', ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(data=top_10_stock, x='col_3', y='col_1', palette='magma')

plt.title('Задача 40: Топ-10 товаров по количеству на складе')
plt.xlabel('Количество (штук)')
plt.ylabel('Наименование товара')
plt.show()

print("--- Топ-10 товаров по запасу ---")
print(top_10_stock[['col_1', 'col_3']])

#41
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['до 50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)

heatmap_data = df.pivot_table(
    index='col_7',
    columns='price_range',
    values='col_1',
    aggfunc='count',
    fill_value=0
)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Количество товаров'})

plt.title('Задача 41: Тепловая карта распределения товаров по ценам и категориям')
plt.xlabel('Ценовой диапазон')
plt.ylabel('Категория (col_7)')

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("--- Сводная таблица данных для Heatmap ---")
print(heatmap_data)

#42
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_5'] = pd.to_numeric(df['col_5'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='col_2', y='col_5',
            scatter_kws={'alpha':0.5},
            line_kws={'color':'red'})

plt.title('Задача 42: Взаимосвязь цены и рейтинга товаров')
plt.xlabel('Цена товара (col_2)')
plt.ylabel('Рейтинг товара (col_5)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

#43
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('catalog_analysis.xlsx')

numeric_columns = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=numeric_columns)

sns.set_theme(style="ticks")
g = sns.pairplot(df, vars=['col_2', 'col_3', 'col_4', 'col_5'], hue='col_7')
plt.show()

#44
import pandas as pd
import numpy as np

df = pd.read_excel('catalog_analysis.xlsx')

df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

mean_price, std_price = df['col_2'].mean(), df['col_2'].std()
mean_stock, std_stock = df['col_3'].mean(), df['col_3'].std()

price_outliers = df['col_2'] > (mean_price + 3 * std_price)
stock_outliers = df['col_3'] > (mean_stock + 3 * std_stock)

extreme_items = df[price_outliers | stock_outliers]

print("--- Задача 44: Аномальные товары ---")
print(f"Найдено аномалий: {len(extreme_items)}")
print(extreme_items[['col_1', 'col_2', 'col_3']].head())

#45
import pandas as pd

df = pd.read_excel('catalog_analysis.xlsx')
for col in ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
category_summary = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    total_stock=('col_3', 'sum')
).reset_index()
top_10_stock = df.sort_values(by='col_3', ascending=False).head(10)
top_10_price = df.sort_values(by='col_2', ascending=False).head(10)
with pd.ExcelWriter('catalog_final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Финальный отчет', index=False)

    category_summary.to_excel(writer, sheet_name='Сводка по категориям', index=False)

    top_10_stock.to_excel(writer, sheet_name='Топ-10 по запасам', index=False)

    top_10_price.to_excel(writer, sheet_name='Топ-10 по стоимости', index=False)

print("--- Задача 45 завершена ---")
print("Файл 'catalog_final_report.xlsx' готов к презентации.")
'''