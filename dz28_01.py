avop = ['+','-','*','/'] #доступні операції
stopword = ["стоп","stop"]
a = []

def stopdet(b):
    for i in b:
        if str(i).lower() in stopword:  # Перевіряємо, чи елемент є у списку стоп-слів
            return False  # Якщо знайшли слово зі стоп-листа, повертаємо False
    return True  # Якщо всі елементи пройшли перевірку, повертаємо True
###################
try:
    while len(a) < 3:
        insert0 = input("введіть перше число\n")
        if stopdet(a):
            a.insert(0, int(insert0))
        else:
            break

        a.insert(1, input("введіть дію\nдоступні дії:'+','-','*','/'\n"))
        if not stopdet(a):
            break
        if a[1] not in avop:
            print("вказаної вами дії немає в доступних")
            a.clear()
            continue

        insert2 = input("введіть друге число\n")
        if stopdet(a):
            a.insert(2, int(insert2))
        else:
            break
except ValueError:
    print("Це не цифра")
#######################

if a[1] == '+':
    c = a[0] + a[2]
    print(*a, "=", c)
elif a[1] == '-':
    c = a[0] - a[2]
    print(*a, "=", c)
elif a[1] == '*':
    c = a[0] * a[2]
    print(*a, "=", c)
elif a[1] == '/':
    if a[2] == 0:
        print("На нуль ділити не можна")
        c=0
    else:
        c = a[0] / a[2]
        print(*a, "=", c)