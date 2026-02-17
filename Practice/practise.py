#1
with open("new_file", "w", newline="", encoding="utf-8") as f1:
    f1.write("akzhan\n")
    f1.write("python")

with open("new_file", "r", encoding="utf-8") as f1:
    content = f1.read()
    print(content)


