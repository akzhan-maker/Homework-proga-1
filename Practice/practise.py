#1
with open("new_file", "w", newline="", encoding="utf-8") as f1:
    f1.write("akzhan\n")
    f1.write("python")

with open("new_file", "r", encoding="utf-8") as f1:
    content = f1.read()
    print(content)

#2
with open("data_file", "w", newline="", encoding="utf-8") as f1:
    for i in range(1,10):
        f1.write(str(i) + "\n")

with open("data_file", "r", encoding="utf-8") as f1:
    content = f1.read()
    print(content)

#3
text = input()
words = text.split()
with open("names-upper", "w", encoding="utf-8") as f1:
    for word in words:
        f1.write(word.upper() + "\n")

print()
with open("names-upper", "r", encoding="utf-8") as f1:
    for line in f1:
        print(line.strip().upper())

#4
import csv
with open("new_file", "w", newline="", encoding="utf-8") as f1:
    f1.write("akzhan\n")
    f1.write("python")

with open("new_file", "r", encoding="utf-8") as f1:
    content = f1.read()
    print(content)

#5
import csv

with open("new_file.csv", "w", newline="", encoding="utf-8") as f1:
    writer = csv.writer(f1)
    writer.writerow(["akzhan"])
    writer.writerow(["python"])

with open("new_file.csv", "r", encoding="utf-8") as f1:
    reader = csv.reader(f1)
    for row in reader:
        print(row[0])


