def sum_deep(l):
    if len(l) == 1:
        if type(l[0]) is list:
            return sum_deep(l[0])
        else:
            if type(l[0]) == int or type(l[0]) == float:
                return l[0]
            else:
                return 0
    else:
        if type(l[0]) == int or type(l[0]) == float:
            return l[0] + sum_deep(l[1:])
        elif type(l[0]) is list:
            return sum_deep(l[0]) + sum_deep(l[1:])
        elif type(l[0]) is tuple:
            s = 0
            for x in l[0]:
                if type(x) == int or type(x) == float:
                    s += x
            return s + sum_deep(l[1:])
        else:
            return sum_deep(l[1:])


list1 = [3, 4, 'hello', (4.6, 5.6, 'text'), [3, 7, 2, 2, [0.3, [5]], 'text'], 6, 3, 3.5, ['text', 1, (1.5)]]
print(sum_deep(list1))
