# -*- coding: utf-8 -*-

import msvcrt
import random

words=['ヘキセン','ブタン']
index = 0



question = words[random.randint(0,1)]
print(question)

while index < len(question):
    key = msvcrt.getch().decoe("utf-8")

    print(key, end="", flush=True)

    if key == question[index]:
        index += 1
    else:
        print('\nミス！最初から')
        index = 0

print('\nクリア!')
