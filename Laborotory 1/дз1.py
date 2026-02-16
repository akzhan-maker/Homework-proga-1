
#1
def analyze_text(text):
    vowels = "aeiouyаеёиоуыэюя"
    used_vowels = ""
    clean = ""
    for c in text:
        if c.isalpha() or c == " ":
            clean += c.lower()
    for c in clean:
        if c in vowels and c not in used_vowels:
            used_vowels += c
    words = clean.split()
    result = ""
    for w in words:
        if len(w) >= 5 and w[0] == w[-1]:
            if w not in result:
                result += w + " "
    return len(used_vowels), result.strip()
print("1 — вести текст:")
choice = int(input())
if choice == 1:
    text = input("Введите текст: ")
    print(analyze_text(text))  # Вывод :


#2
process_string = lambda s: " ".join([ word[::-1]
    for word in s.split()
    if not any(char.isdigit() for char in word)
    and len(word) % 2 == 0])
text_input = input("Введите строку: ")
result = process_string(text_input)
print("Результат:", result)   # Вывод :

#3
def top_k_words(text, k):
    text = text.lower()
    marks = '.,!?;:-()"'
    clean_text = ""
    for char in text:
        if char not in marks:
            clean_text += char
    words = clean_text.split()
    unique_words = []
    counts = []
    for w in words:
        if w in unique_words:
            index = unique_words.index(w)
            counts[index] += 1
        else:
            unique_words.append(w)
            counts.append(1)
    combined = []
    for i in range(len(unique_words)):
        combined.append([unique_words[i], counts[i]])
    combined.sort()
    combined.sort(key=lambda x: x[1], reverse=True)  # Вывод :

#4
def analyze_text(text):
    clean_chars = ()
    vowels = set("ауоыиэяюе")
    found_vowels = set()
    for char in clean_chars:
        if char in vowels:
            found_vowels.add(char)
    count_vowels = len(found_vowels)
    words = text.split()
    found_words_list = []
    seen_words = set()
    for word in words:
        clean_word = "".join(char.lower() for char in word if char.isalpha())
        if len(clean_word) >= 5 and clean_word not in seen_words:
            if clean_word and clean_word[0] == clean_word[-1]:
                found_words_list.append(clean_word)
                seen_words.add(clean_word)
    words_str = " ".join(found_words_list)
    return (count_vowels, words_str)
text_example = "Арбуз бобАрбуз, Привет! КазаК и БараБан. Анна, потоП"
print(analyze_text(text_example))   # Вывод: (0, 'казак потоп')

#5
def compress_text(text):
    if not text:
        return ""

    result = []
    count = 1
    start_char = text[0]

    for i in range(1, len(text)):
        if text[i].lower() == text[i-1].lower():
            count += 1
        else:
            result.append(start_char)
            if count > 1:
                result.append(str(count))
            count = 1
            start_char = text[i]
    result.append(start_char)
    if count > 1:
        result.append(str(count))
    return "".join(result)
print(compress_text("aaBBcDDD"))  # Вывод: a2B2cD3

#6
filter_words = lambda text: [
    word for word in text.split()
    if len(word) >= 4
    and word.isalpha()
    and len(set(word.lower())) == len(word)]
test_string = "Apple juice is cold and tasty123 but melon is fresh"
result = filter_words(test_string)
print(result) # Вывод : ['juice', 'cold', 'melon', 'fresh']

#7
import string
def palindrome_words(text):
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()
    palindromes = set()
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3 and word_lower == word_lower[::-1]:
            palindromes.add(word_lower)
    result = sorted(list(palindromes), key=lambda x: (-len(x), x))
    return result

text = "Дед идет по лесу и собирает грибы для казак"
print(palindrome_words(text)) # Вывод :['казак', 'дед']

#8
VOWELS = "aeiouyаеёиоуыэюя"
categorize_words = lambda text: " ".join([
    word if any(char.isdigit() for char in word)
    else "VOWEL" if word[0].lower() in VOWELS
    else "CONSONANT"
    for word in text.split()])
test_text = "Apple b4nana orange tomato 123py"
result = categorize_words(test_text)
print(result)
# Вывод: VOWEL b4nana VOWEL CONSONANT 123py


#9
def alternate_case_blocks(text, n):
    text = text.replace(" ", "")
    result = []
    block_index = 0
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if block_index % 2 == 0:
            result.append(block.upper())
        else:
            result.append(block.lower())
        block_index += 1
    return "".join(result)
print(alternate_case_blocks("HelloopsWorld", 3))  # Вывод: "HELlooSWOrld"
print(alternate_case_blocks("Python is great", 2))  # Вывод : "PYthONisGReaT"


#10
count_special_words = lambda text: sum(
    1 for word in text.split()
    if len(word) >= 5
    and not word[0].isdigit()
    and any(char.isdigit() for char in word))
test_text = "Python3 version 3.10 is great but 1password and secret2024 are different"
result = count_special_words(test_text)
print(result)   # Вывод : 2


#11
def common_unique_chars(s1, s2):
    set2 = set(s2)
    result = []
    added = set()
    for char in s1:
        if (char in set2 and
            char not in added and
            char != " " and
            not char.isdigit()):
            result.append(char)
            added.add(char)
    return "".join(result)
string1 = "hello world 123"
string2 = "gold rose 456"
print(common_unique_chars(string1, string2))
# Вывод: "elrod"

#12
filter_complex_words = lambda text: [
    word for word in text.split()
    if len(word) > 3
    and word[0].lower() == word[-1].lower()
    and word.lower() != word.lower()[::-1]]
test_text = "level alaska radar window area anna"
result = filter_complex_words(test_text)
print(result)
# Вывод: ['alaska', 'window', 'area']

#13
def replace_every_nth(text, n, char):
    words = text.split(' ')
    result_words = []
    global_counter = 0
    for word in words:
        new_word = list(word)
        if len(word) >= 3:
            for i in range(len(new_word)):
                if not new_word[i].isdigit():
                    global_counter += 1
                    if global_counter % n == 0:
                        new_word[i] = char
        result_words.append("".join(new_word))
    return " ".join(result_words)
text = "Apple 123 banana is tasty"
print(replace_every_nth(text, 2, "*")) # Вывод:(A*p*e 123 *a*a*a is *a*t*)


#14
VOWELS = "aeiouyаеёиоуыэюя"
filter_unique_words = lambda text: ", ".join([
    word for word in text.split()
    if len(set(word.lower())) > 3 and (
        vowel_list := [c for c in word.lower() if c in VOWELS],
        len(vowel_list) == len(set(vowel_list)))[1]])
test_text = "Apple orange banana cucumber python melody"
result = filter_unique_words(test_text)
print(result)
# Вывод: orange, cucumber, python, melody


#15
def word_pattern_sort(text):
    words = text.split()
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    VOWELS = "aeiouyаеёиоуыэюя"
    result = []
    for length in sorted(groups.keys()):
        group = groups[length]
        group.sort(key=lambda w: (
            -sum(1 for char in w.lower() if char in VOWELS),
            w.lower()))
        result.extend(group)
    return result
test_text = "apple banana kiwi art egg orange"
print(word_pattern_sort(test_text)) # Вывод:['art', 'egg', 'kiwi', 'apple', 'banana', 'orange']

#16
def transform_list(nums):
    result = []
    for x in nums:
        if x < 0:
            continue
        if x % 2 == 0:
            result.append(x ** 2)
        elif x > 10:
            sum_digits = sum(int(digit) for digit in str(x))
            result.append(sum_digits)
        else:
            result.append(x)
    return result
numbers = [-5, 4, 11, 7, 22, 3]
print(transform_list(numbers)) # Вывод: [16, 2, 7, 484, 3]

#17
process_nums = lambda nums: list(map(lambda x: x**2, filter(lambda x:
    (x % 3 == 0 or x % 5 == 0) and
    (x % 15 != 0) and
    (len(str(abs(x))) % 2 != 0),
    nums)))
test_list = [3, 5, 9, 15, 30, 100, 250, 1245]
print( process_nums(test_list)) # Вывод: [9, 25, 81, 10000, 62500]

#18
def flatten_and_filter(lst):
    flat_list = []
    def extract(items):
        for item in items:
            if isinstance(item, list):
                extract(item)
            else:
                flat_list.append(item)
    extract(lst)
    result = []
    for n in flat_list:
        if n > 0 and n % 4 != 0 and len(str(abs(n))) > 1:
            result.append(n)
    return sorted(result)
nested = [1, [12, 13, -5], [[4, 21], 101], 7]
print( flatten_and_filter(nested)) # Вывод: [13, 21, 101]

#19
find_even_pairs = lambda list1, list2: [
    a for a, b in zip(list1, list2)
    if a == b and a % 2 == 0]
list_a = [2, 4, 10, 8, 14]
list_b = [2, 5, 10, 7, 14]
print( find_even_pairs(list_a, list_b)) # Вывод: [2, 10, 14]

#20
def max_subarray_sum(nums, k):
    max_sum = -1
    found = False
    for i in range(len(nums) - k + 1):
        window = nums[i: i + k]
        is_valid = True
        current_sum = 0
        for x in window:
            if x <= 0:
                is_valid = False
                break
            current_sum += x
        if is_valid:
            if current_sum > max_sum:
                max_sum = current_sum
            found = True
    return max_sum if found else None
numbers = [1, 2, 3, -1, 4, 5, 0, 6, 7]
k = 2
result = max_subarray_sum(numbers, k)
print( result)  # Вывод: 13


#21
task_21 = lambda strings: [s.upper() for s in strings
if s.isalpha() and len(s) > 4 and len(set(s.lower())) == len(s)]

print(task_21(["Python", "Java", "Apple", "Abcde", "Swift"]))
# вывод: ['PYTHON', 'ABCDE', 'SWIFT']

#22
def group_by_parity_and_sort(nums):
    evens = sorted([n for n in nums if n % 2 == 0])
    odds = sorted([n for n in nums if n % 2 != 0])
    return evens + odds

print(group_by_parity_and_sort([5, 2, 9, 1, 4, 8, 3]))
# вывод: [2, 4, 8, 1, 3, 5, 9]

#23
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
task_23 = lambda nums: [val for i, val in enumerate(nums)
if is_prime(i) and val % 2 != 0 and val > (sum(nums) / len(nums) if nums else 0)]

print(task_23([10, 2, 15, 7, 2, 20]))
# вывод: [15]


#24
def longest_increasing_sublist(nums):
    if not nums: return []
    max_sub, current_sub = [], [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_sub.append(nums[i])
        else:
            if len(current_sub) > len(max_sub): max_sub = current_sub
            current_sub = [nums[i]]
    return current_sub if len(current_sub) > len(max_sub) else max_sub

print(longest_increasing_sublist([1, 2, 3, 0, 4, 5, 6, 7, 2]))
# вывод: [0, 4, 5, 6, 7]


#25
task_25 = lambda lists: [sum(lst) / len(lst) for lst in lists if len(lst) >= 3 and sum(lst) % 2 == 0]

print(task_25([[1, 2, 3], [10, 20], [2, 2, 2, 2]]))
# вывод: [2.0, 2.0]


#26
def remove_duplicates_keep_last(nums):
    res, seen = [], set()
    for n in reversed(nums):
        if n not in seen:
            res.append(n)
            seen.add(n)
    return res[::-1]

print(remove_duplicates_keep_last([1, 2, 1, 3, 2, 4]))
# вывод: [1, 3, 2, 4]


#27
task_27 = lambda strings: sorted(strings, key=lambda s: (-len(s), s))[:5]

print(task_27(['яблоко', 'арбуз', 'банан', 'еж', 'ананас', 'антилопа']))
# вывод: ['антилопа', 'ананас', 'яблоко', 'арбуз', 'банан']


#28
def moving_average(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        if all(x >= 0 for x in window): res.append(sum(window) / k)
    return res

print(moving_average([1, 2, 3, -1, 4, 5], 2))
# вывод: [1.5, 2.5, 4.5]


#29
task_29 = lambda l1, l2: [x for x in l1 if x not in l2 and x > (sum(l1) / len(l1) if l1 else 0)]

print(task_29([10, 20, 30, 40], [10, 50]))
# вывод: [30, 40]


#30
def analyze_strings_list(words):
    res, seen = [], set()
    for s in words:
        if any(c.isdigit() for c in s): continue
        new_s = s[::-1] if len(s) % 2 == 0 else s.upper()
        if new_s not in seen:
            res.append(new_s)
            seen.add(new_s)
    return res

print(analyze_strings_list(['abc', 'abcd', 'a1', 'abc', 'defg']))
# вывод: ['ABC', 'dcba', 'gfed']

