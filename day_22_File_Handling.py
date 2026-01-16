from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate (items):
         print(f"{i+1}: {items}")


def createfile():
    readfileandfolder()


print("press 1 for create file ")
print("press 2 for reading a file ")
print("press 3 fo updating  a file ")
print("press 4 for deleting  a file ")



check = int(input("please tell your response - "))
1
