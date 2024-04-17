#! /usr/bin/env python
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---
     1 X 1 = 1
     2 X 1 = 2
     3 X 1 = 3
...
######################
---Tabuada do 2---
      2 X 1 = 2
      2 X 2 = 4
   ...
###################### 
"""
__version__ = "0.1.1"
__author__ = "Cesar Rocha"

template = """
---Tabuada do {n1}---

{bloco:^30}
    
"""

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}\n"))
    print("#" *18)
        