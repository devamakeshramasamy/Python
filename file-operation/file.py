f = open(r"D:\Python\Python\file-operation\file1.py", "w")
f.write("hello")
f.close()

fr = open(r"D:\Python\Python\file-operation\file1.py", "r+")
print(fr.read())
fr.close()
