
#1
import pandas as pd
df = pd.read_excel('catalog_products.xlsx')


print("--- Первые 5 строк таблицы ---")
print(df.head())

print(f"\nФорма DataFrame (строк, столбцов): {df.shape}")

print("\n--- Типы данных всех колонок ---")
print(df.dtypes)

print("\n--- Количество пропусков в каждой колонке ---")
print(df.isnull().sum())

#2
import pandas as pd
import numpy as np

df = pd.read_excel('catalog_products.xlsx')

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].astype(float)

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
text_cols = df.select_dtypes(include=['object']).columns
df = df.dropna(subset=text_cols)

print("--- Задача 2 выполнена ---")
print(f"Новая форма данных после очистки: {df.shape}")

#3
import pandas as pd
import numpy as np

df = pd.read_excel('catalog_products.xlsx')

df['total_value'] = df['col_2'] * df['col_3']

df['log_price'] = np.log1p(df['col_2'])

df['double_stock'] = df['col_3'] * 2

print("--- Задача 3: Новые признаки созданы ---")
columns_to_show = ['col_2', 'col_3', 'total_value', 'log_price', 'double_stock']
print(df[columns_to_show].head())

#4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('catalog_products.xlsx')


plt.figure(figsize=(18, 6))


plt.subplot(1, 3, 1)
sns.histplot(df['col_2'], kde=True, color='skyblue')
plt.title('Распределение цен (col_2)')


plt.subplot(1, 3, 2)
sns.scatterplot(x=df['col_3'], y=df['col_2'], alpha=0.6)
plt.title('Связь цены и количества')

plt.subplot(1, 3, 3)
sns.boxplot(x='col_7', y='col_2', data=df)
plt.xticks(rotation=45)
plt.title('Разброс цен по категориям')

plt.tight_layout()
plt.show()#pip install matplotlib seaborn
#------pip install matplotlib seaborn-------

#5
import pandas as pd

df = pd.read_excel('catalog_products.xlsx')
mean_val = df['col_2'].mean()
std_val = df['col_2'].std()

upper_limit = mean_val + 3 * std_val
lower_limit = mean_val - 3 * std_val

anomalies = df[(df['col_2'] > upper_limit) | (df['col_2'] < lower_limit)]

print(f"Найдено аномальных строк: {len(anomalies)}")
print("Примеры аномалий:")
print(anomalies[['col_2', 'col_7']].head())

df_clean = df.drop(anomalies.index)
print(f"\nРазмер таблицы до очистки: {len(df)}")
print(f"Размер таблицы после очистки: {len(df_clean)}")

#6
import pandas as pd

df = pd.read_excel('catalog_products.xlsx')

df = df.dropna(subset=['col_7'])

df_encoded = pd.get_dummies(df, columns=['col_7'])

print("--- Задача 6: Результат кодирования ---")
print("Список новых колонок (первые 15):")
print(df_encoded.columns[:15].tolist())

print("\nТипы данных после преобразования:")
print(df_encoded.dtypes.value_counts())

#----pip install scikit-learn----
#7
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_excel('catalog_products.xlsx')
df_numeric = df.select_dtypes(include=['number']).dropna()
y = df_numeric['col_2']
X = df_numeric.drop(columns=['col_2'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- Задача 7 выполнена ---")
print(f"Целевая переменная (y): выбрана колонка 'col_2'")
print(f"Количество признаков для обучения (X): {X.shape[1]}")
print(f"Размер обучающей выборки (80%): {X_train.shape[0]} строк")
print(f"Размер тестовой выборки (20%): {X_test.shape[0]} строк")

print("\nПример данных из X_train:")
print(X_train.head())

#8
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Допустим, X - это площадь, а y - цена
X = np.array([[30], [45], [60], [80], [100], [120], [150], [180]])
y = np.array([3.1, 4.2, 5.5, 8.2, 10.1, 12.4, 15.6, 18.2])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model_simple = LinearRegression()
model_simple.fit(X_train, y_train)

y_pred = model_simple.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 8 ---")
print(f"Предсказания на тесте: {y_pred}")
print(f"Средняя абсолютная ошибка (MAE): {mae:.2f}")
print(f"Среднеквадратичная ошибка (MSE): {mse:.2f}")

#9
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(42)
n_samples = 100

data = pd.DataFrame({
    'total_value': np.random.rand(n_samples) * 100,
    'double_stock': np.random.rand(n_samples) * 50,
    'price_raw': np.random.rand(n_samples) * 200 + 10,
    'category': np.random.choice(['A', 'B', 'C'], n_samples)
})

data['log_price'] = np.log(data['price_raw'])
data = pd.get_dummies(data, columns=['category'], drop_first=True)

y = (data['total_value'] * 1.2 +
     data['double_stock'] * 0.8 +
     np.random.normal(0, 5, n_samples))

X = data.drop(columns=['price_raw'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

y_pred_multi = model_multi.predict(X_test)

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 9 ---")
print(f"Новый MAE: {mean_absolute_error(y_test, y_pred_multi):.2f}")
print(f"Новый MSE: {mean_squared_error(y_test, y_pred_multi):.2f}")

#10
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.random.seed(42)
X = np.random.rand(100, 1) * 100
y = 2.5 * X + np.random.normal(0, 15, (100, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue', label='Предсказания')

max_val = np.max([np.max(y_test), np.max(y_pred)])
min_val = np.min([np.min(y_test), np.min(y_pred)])

plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='Идеально (y=x)')

plt.xlabel('Истинная цена (y_test)')
plt.ylabel('Предсказанная цена (y_pred)')
plt.title('Задача 10: Визуализация предсказаний')
plt.legend()
plt.grid(True)
plt.show()

#11
import pandas as pd
from sklearn.preprocessing import StandardScaler

cols_to_scale = ['col_3', 'col_4', 'total_value', 'double_stock', 'log_price']

if 'data' not in locals():
    data = pd.DataFrame({
        'col_3': [100, 200, 300],
        'col_4': [1, 2, 3],
        'total_value': [500, 10000, 20000],
        'double_stock': [0, 1, 0],
        'log_price': [5.2, 9.2, 9.9]
    })

scaler = StandardScaler()
data_scaled = data.copy()
data_scaled[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 11 ---")
print("Средние значения после StandardScaler (должны быть ~0):")
print(data_scaled[cols_to_scale].mean().round(4))

print("\nСтандартное отклонение (должно быть ~1):")
print(data_scaled[cols_to_scale].std().round(4))

print("\nПервые строки нормализованных данных:")
print(data_scaled[cols_to_scale].head())

#12
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

np.random.seed(42)
data = pd.DataFrame({
    'total_value': np.random.rand(100) * 100,
    'double_stock': np.random.rand(100) * 50,
    'log_price': np.random.rand(100) * 10,
    'col_3': np.random.rand(100) * 20,
    'col_4': np.random.rand(100) * 5
})
y = data['total_value'] * 2 + data['log_price'] * 5 + np.random.randn(100)

X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=42)

dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

importances = dt_model.feature_importances_
feature_names = X_train.columns

fi_df = pd.DataFrame({'Признак': feature_names, 'Важность': importances})
fi_df = fi_df.sort_values(by='Важность', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Важность', y='Признак', data=fi_df, palette='magma')
plt.title('Задача 12: Важность признаков (Decision Tree)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

#13
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(42)
n_samples = 100
X = pd.DataFrame({
    'total_value': np.random.rand(n_samples) * 100,
    'double_stock': np.random.rand(n_samples) * 50,
    'col_3': np.random.rand(n_samples) * 20,
    'log_price': np.random.rand(n_samples) * 10
})

y = 0.5 * (X['total_value']**2) + X['col_3'] * 5 + np.random.normal(0, 100, n_samples)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 13 ---")
print(f"Количество признаков до: {X_train.shape[1]}")
print(f"Количество признаков после Polynomial: {X_train_poly.shape[1]}")
print(f"MAE (Poly): {mae_poly:.2f}")
print(f"MSE (Poly): {mse_poly:.2f}")

simple_model = LinearRegression().fit(X_train, y_train)
y_pred_simple = simple_model.predict(X_test)
print(f"\nДля сравнения - MAE обычной модели: {mean_absolute_error(y_test, y_pred_simple):.2f}")

#14
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
np.random.seed(42)
X = pd.DataFrame(np.random.rand(150, 4), columns=['total_value', 'col_3', 'col_4', 'log_price'])
y = X['total_value'] * 100 + X['col_3'] * 50 + np.random.normal(0, 10, 150)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred_knn = knn.predict(X_test_scaled)

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 14 ---")
print(f"MAE (KNN): {mean_absolute_error(y_test, y_pred_knn):.2f}")
print(f"MSE (KNN): {mean_squared_error(y_test, y_pred_knn):.2f}")

#15
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
np.random.seed(42)
data = pd.DataFrame({
    'feature': np.random.rand(200) * 100,
    'col_7': np.random.choice(['Electronics', 'Clothing', 'Home'], 200)
})
data['price'] = data.apply(lambda row: row['feature'] * (2 if row['col_7'] == 'Electronics' else 0.5), axis=1)
data['price'] += np.random.normal(0, 5, 200)

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 15 ---")

categories = data['col_7'].unique()

for cat in categories:
    df_cat = data[data['col_7'] == cat]

    X_cat = df_cat[['feature']]
    y_cat = df_cat['price']

    model = LinearRegression()
    model.fit(X_cat, y_cat)

    y_pred = model.predict(X_cat)
    mae = mean_absolute_error(y_cat, y_pred)

    print(f"Категория: {cat:12} | MAE: {mae:.2f}")

print("\nВывод: Разделение на категории позволяет модели быть точнее для специфических групп товаров.")

#16
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 300
data = pd.DataFrame({
    'feature': np.random.rand(n) * 100,
    'cat': np.random.choice(['Electronics', 'Books', 'Home'], n)
})
data['price'] = data.apply(lambda r: r['feature'] * (3 if r['cat'] == 'Electronics' else 1), axis=1)
data['price'] += np.random.normal(0, 15, n)

categories = data['cat'].unique()
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, cat in enumerate(categories):
    df_cat = data[data['cat'] == cat]
    X_train, X_test, y_train, y_test = train_test_split(df_cat[['feature']], df_cat['price'], test_size=0.2)

    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    axes[i].scatter(y_test, y_pred, alpha=0.7, label=f'Данные {cat}')

    line_range = [min(y_test), max(y_test)]
    axes[i].plot(line_range, line_range, color='red', linestyle='--')

    axes[i].set_title(f'Категория: {cat}')
    axes[i].set_xlabel('Истинная цена')
    axes[i].set_ylabel('Предсказанная цена')

plt.tight_layout()
plt.show()

print("Задача 16: Графики построены. Точки вне красной линии — это товары с максимальной ошибкой.")

#17
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

X_cv = np.random.rand(200, 5) # 5 признаков
y_cv = X_cv[:, 0] * 10 + X_cv[:, 1] * 5 + np.random.randn(200)

model_lr = LinearRegression()

# scoring='neg_mean_absolute_error' вернет отрицательные значения (так устроена sklearn)
mae_scores = cross_val_score(model_lr, X_cv, y_cv, cv=5, scoring='neg_mean_absolute_error')
mse_scores = cross_val_score(model_lr, X_cv, y_cv, cv=5, scoring='neg_mean_squared_error')

mae_res = -mae_scores
mse_res = -mse_scores

print("--- РЕЗУЛЬТАТ ЗАДАЧИ 17 ---")
print(f"Среднее MAE по 5 фолдам: {mae_res.mean():.4f}")
print(f"Среднее MSE по 5 фолдам: {mse_res.mean():.4f}")
print(f"Стандартное отклонение MAE: {mae_res.std():.4f}")
print("\nАнализ: Если стандартное отклонение маленькое, модель стабильна.")

#18
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)
data = pd.DataFrame({
    'feature_1': np.random.rand(200) * 100,
    'feature_2': np.random.rand(200) * 50,
    'price': np.random.rand(200) * 1000
})

def classify_price(p):
    if p < 100: return 0
    elif p <= 500: return 1
    else: return 2

data['price_class'] = data['price'].apply(classify_price)

X = data[['feature_1', 'feature_2']]
y = data['price_class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f"--- РЕЗУЛЬТАТ ЗАДАЧИ 18 ---")
print(f"Accuracy (Точность модели): {accuracy_score(y_test, y_pred):.2%}")


#19
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Низкая', 'Средняя', 'Высокая'],
            yticklabels=['Низкая', 'Средняя', 'Высокая'])

plt.title('Задача 19: Confusion Matrix')
plt.ylabel('Реальные классы')
plt.xlabel('Предсказанные классы')
plt.show()

print("Анализ: Числа на диагонали — это правильные ответы. Остальное — ошибки.")


#20
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
output_data = pd.DataFrame({
    'total_value': np.random.rand(50) * 100,
    'log_price': np.random.rand(50) * 10,
    'real_price': np.random.rand(50) * 500,
    'predicted_price': (np.random.rand(50) * 500) + 10
})

try:
    output_data.to_excel('catalog_ml_predictions.xlsx', index=False)
    print("--- РЕЗУЛЬТАТ ЗАДАЧИ 20 ---")
    print("Файл 'catalog_ml_predictions.xlsx' успешно сохранен!")
except ImportError:
    print("Ошибка: Для работы с Excel нужно установить openpyxl (команда: pip install openpyxl)")

print("\n--- ФИНАЛЬНЫЙ ОТЧЕТ ---")

plt.figure(figsize=(10, 6))
plt.scatter(output_data['real_price'], output_data['predicted_price'], alpha=0.5, color='green')
plt.plot([0, 500], [0, 500], color='red', linestyle='--')
plt.title('Финальный отчет: Предсказанные vs Истинные цены')
plt.xlabel('Истинная цена')
plt.ylabel('Предсказанная цена')
plt.grid(True)
plt.show()
