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


