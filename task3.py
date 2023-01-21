
FILES_TO_READ = ["1.txt", "2.txt", "3.txt", "4.txt"]

def insert_into_list(fl, name, lines):
    if not len(fl): fl.append([name, lines])
    elif len(lines) < len(fl[0][1]): fl.insert(0, [name, lines])
    elif len(lines) > len(fl[-1][1]): fl.append([name, lines])
    else:
        for i in range(len(fl) - 1):
            if len(fl[i][1]) < len(lines) < len(fl[i + 1][1]):
                fl.insert(i + 1, [name, lines])
                break

file_list = []
for f in FILES_TO_READ:
    with open(f, encoding="utf-8") as inf:
        lines = inf.readlines()
    insert_into_list(file_list, f, lines)
for name, lines in file_list:
    print(f"{name}\n{len(lines)}")
    for line in lines: print(line.strip())