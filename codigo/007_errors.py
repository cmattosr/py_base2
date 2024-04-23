#!/usr/bin/env python3

import sys
import os

# LBYL - Look Before You Leap
# if os.path.exists("007_names.txt"):
#     print("File found")
#     input("...") # race condition
#     names = open("007_names.txt").readlines()
# else:
#     print("Error: File names.txt not found")
#     sys.exit(1)

# LBYL - Look Before You Leap
# if len(names) >= 3:
#     print(names[2])
# else:
#     print("Error: Missing name in the list")
#     sys.exit(1)
    
#EAFP - Easier to Ask Forgiveness than Permission
try:
    names = open("007_names.txt").readlines() # FileNotFoundError
    # 1 / 0 # ZeroDivisionError
    # print(names.banana) # AttributeError
except FileNotFoundError as e:
    # print("Error: File names.txt not found")
    print(str(e))
    sys.exit(1)
except ZeroDivisionError:
    print("Error: Daivision by zero")
    sys.exit(1)
except AttributeError:
    print("Error: Attribute not found")
    sys.exit(1)
    
try:
    print(names[1])
except:
    print("Error: Missing name in the list")
    sys.exit(1)
else:
    print("Name found")
finally:
    print("Finally")