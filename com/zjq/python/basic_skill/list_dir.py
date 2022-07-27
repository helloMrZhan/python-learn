# 稳定排序地遍历一个文件下的文件

import os

def ordered_list_dir(dir):
    entries = os.listdir(dir)
    entries.sort()
    return entries

if __name__ == '__main__':
    entries = ordered_list_dir('./')
    for entry in entries:
        print(entry)