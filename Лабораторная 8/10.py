a = ["scan", "debug_mode", "scan", "connect", "debug_info"]
b = set()   # пустое множество
for c in a:                     # смотрим каждую команду
    if "debug" not in c:           # если нет слова debug
        b.add(c)      # добавляем в множество
print(b)