
#1.1
check = lambda x: "ok" if x > 0 else ("not ok" if x < 0 else "zero")

print(check(5))
print(check(-3))
print(check(0))

#1.2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sortedwords= sorted(words, key=lambda x: (len(x),x))
print(sortedwords)

#1.3
numbers = [5, 12, 7, 20, 33, 8]
filtered_numbers = list(filter(lambda x: x % 2 != 0 and x>10, numbers))
print(filtered_numbers)

#1.4
numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = list(map(lambda x: x**2 if x % 2 == 0 else x*3, numbers))
print(filtered_numbers)

import numbers

#1.5
a = int(input("Enter a: "))
b = int(input("Enter b: "))
compare = lambda x, y: 'a is lower' if x < y else ('b is lower' if y < x else 'a and b are the same')
result = compare(a, b)
print(result)

#1.6
numbers = [0, -3, 5, -7, 8]
filtered_numbers = list(map(lambda x: 'ok' if x>0 else('not ok' if x<0 else 'zero'),numbers))
print(filtered_numbers)

#2.1
def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            if i % 4 == 0:
                yield "кратно 4"
            else:
                yield i
for x in even_numbers(10):
    print(x)

#2.2
def filter_words(words_list):
    for w in words_list:
        if len(w) >= 4:
             yield w
        if 'а' in w.lower():
            yield 'с а'
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)

#2.3
def infinite_numbers():
    n = 1
    while True:
        if n % 3 == 0 and n % 5 == 0:
            yield "FizzBuzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield n
        n += 1
gen = infinite_numbers()
for a in range(10):
    print(next(gen))

#2.4
def squares(n):
    for i in range(1, n + 1):
        sq = i ** 2
        if sq % 2 == 0:
            yield "чётный квадрат"
        else:
            yield sq
for x in squares(5):
    print(x)

#3.1
squares = [x**2 for x in range(1, 21) if x % 2 == 0]

print(squares)

#3.2
from functools import reduce

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
products = [reduce(lambda x, y: x * y, row) for row in matrix]

print(products)

#3.3
words = ["кот", "машина", "ананас", "дом", "компьютер", "скрипт"]
filtered_words = [w for w in words if len(w) > 4 if 'а' not in w.lower()]

print(filtered_words)

#3.4
numbers = [1, 2, 3, 4, 5]
result_dict = {n: "четное" if n % 2 == 0 else "нечетное" for n in numbers}

print(result_dict)

#3.5
matrix = [[1, 2], [3, 4], [5, 6]]
flatten_list = [item for row in matrix for item in row]

print(flatten_list)

#3.6
numbers = list(range(1, 21))
fizzbuzz_list = [
    "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else
    "Fizz" if x % 3 == 0 else
    "Buzz" if x % 5 == 0 else
    x
    for x in numbers
]

print(fizzbuzz_list)

#4.1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def special_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i

for x in special_numbers(15):
    print(x)

#4.2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
processed_words = [
    (lambda w: (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w.lower() else ""))(word)
    for word in words
]

print(processed_words)

#4.3
def process_numbers(numbers):
    positive_numbers = filter(lambda x: x >= 0, numbers)

    transformed = map(lambda x: x / 2 if x % 2 == 0 else x * 3 + 1, positive_numbers)

    for val in transformed:
        yield val
numbers = [5, -2, 8, 0, -7, 3]
for x in process_numbers(numbers):
    print(x)

#4.4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]

get_grade_level = lambda score: "Отлично" if score >= 90 else ("Хорошо" if score >= 70 else "Удовлетворительно")

grades_dict = {name: get_grade_level(score) for name, score in students}

print(grades_dict)

#4.5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def matrix_transform(matrix):
    for row in matrix:
        for num in row:
            if num % 2 == 0 and num % 3 == 0:
                yield "кратно 6"
            elif num % 2 == 0:
                yield "чётное"
            elif num % 3 == 0:
                yield "кратно 3"
            else:
                yield num

for x in matrix_transform(matrix):
    print(x)

#5.1
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print(doubled)
# Ожидаемый результат: [2, 4, 6, 8, 10]

#5.2
words = ["кот", "машина", "арбуз", "дом"] 
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))

print(result)

#5.3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

#5.4
numbers = [0, 5, 12, 7, 20, -3, 8] 
result = list(map(lambda x: x / 2 if x % 2 == 0 else x * 3, 
                  filter(lambda x: x > 5, numbers)))

print(result)