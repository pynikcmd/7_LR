#!/isr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input("Введите 10 элементов: ").split()))

    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Определить индексы мин элемента.
    A_min = A[0]
    i_min = 0
    for i, item in enumerate(A):
        if item < A_min:
            i_min, A_min = i, item

    # Поменять местами мин элемент с последним.
    A[i_min] = A[-1]
    A[-1] = A_min

    print(A)
