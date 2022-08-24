import os
from os.path import join, getsize
from pathlib import Path


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

pian = Path("D:/pian")
listpiandir = [each for each in pian.iterdir() if each.is_dir()]
result = []
i = 0
for x in listpiandir:
    if getdirsize(x) < 50 * 1024 * 1024:
        print(f"{x.name}文件夹大小{getdirsize(x) / 1024 / 1024}Mbytes")
        result.append(x)
        i += 1
        print(f"正在删除{x.name}文件夹...第{i}个")
        for root1, dirs1, files1 in os.walk(x):
            for name1 in files1:
                os.remove(os.path.join(root1, name1))
            for name2 in dirs1:
                os.rmdir(os.path.join(root1, name2))
        x.rmdir()
print(result, f"共计统计并删除{len(result)}个文件夹", sep="\n")



    
