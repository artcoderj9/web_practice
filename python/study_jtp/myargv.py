# myargv.py

import sys

a = sys.argv
result = 0
for i in range(1, len(a)):
    result += int(a[i])

print(result)