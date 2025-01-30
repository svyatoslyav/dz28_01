avop = ['+','-','*','/'] #доступні операції
stopword = ["стоп","stop"]
a = []
print("Введіть стоп або stop для завершення")
def stopdet(b):
    for i in b:
        if str(i).lower() in stopword:  # Перевіряємо, чи елемент є у списку стоп-слів
            return False  # Якщо знайшли слово зі стоп-листа, повертаємо False
    return True  # Якщо всі елементи пройшли перевірку, повертаємо True
while stopdet(a):
    ###################
    try:
        while len(a) < 3:
            insert0 = input("введіть перше число\n")
            if insert0.lower() not in stopword:
                a.insert(0, int(insert0))
            else:
                a.insert(0, insert0)
                break

            a.insert(1, input("введіть дію\nдоступні дії:'+','-','*','/'\n"))
            if not stopdet(a):
                break
            if a[1] not in avop:
                print("вказаної вами дії немає в доступних")
                a.clear()
                continue

            insert2 = input("введіть друге число\n")
            if insert2.lower() not in stopword:
                a.insert(2, int(insert2))
            else:
                a.insert(0, insert2)
                break

    except ValueError:
        print("Це не число")
        a.clear()
        continue
    #######################
    if len(a) == 3:
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
            else:
                c = a[0] / a[2]
                print(*a, "=", c)

    if stopdet(a):
        a.append(input("Продовжити?(введіть стоп або stop щоб завершити)\n"))
        a.clear()
    else:
        break
