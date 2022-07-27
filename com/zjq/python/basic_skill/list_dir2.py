# 遍历一个文件夹下的所有子文件夹，并返回所有'config.json'文件的绝对路径列表

import os

def retrieve_file_paths(dir_name):
    file_paths = []
    abs_dir_name = os.path.abspath(dir_name)

    # 在此实现遍历代码
    for base, dirs, files in os.walk(abs_dir_name):
        for dir in dirs:
            cfg_file = os.path.join(base, dir, 'config.json')
            if os.path.exists(cfg_file):
                file_paths.append(cfg_file)

    return file_paths

if __name__ == '__main__':
    file_paths = retrieve_file_paths('./')
    print(file_paths)