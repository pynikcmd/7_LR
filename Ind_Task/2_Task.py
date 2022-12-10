#!/isr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = list(map(float, input("Введите числа: ").split(' ')))
    count = 0

    # Количество элементов списка, лежащих в диапазоне от А до В.
    A = float(input("Введите 1 число: "))
    B = float(input("Введите 2 число: "))
    for i in s:
        if A <= i <= B:
            count += 1

    maxi = max(s)
    summ = sum(s[s.index(maxi) + 1:])

    print(summ)
    print(count)
