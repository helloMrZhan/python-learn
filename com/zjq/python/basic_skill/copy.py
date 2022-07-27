# 实现文件夹拷贝，要求如下：
#
# 使用 shutil 拷贝 "copy.py" 文件到 "/tmp/copy.py"
# 拷贝 "copy.py" 文件到 "/tmp/copy2.py", 保留元数据
# 递归拷贝目录 "./" 到 "/tmp/file_test/"，如果已存在就覆盖

import shutil

def test():
    # 拷贝文件
    shutil.copy(
        "copy.py",
        "/tmp/copy.py"
    )

    # 拷贝文件，保持元数据
    shutil.copy2(
        "copy.py",
        "/tmp/copy2.py"
    )

    # 递归拷贝目录
    shutil.copytree(
        "./",
        "/tmp/file_test/",
        dirs_exist_ok=True
    )

if __name__ == '__main__':
    test()