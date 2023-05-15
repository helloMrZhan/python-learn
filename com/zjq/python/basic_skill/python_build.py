# 打印出 Python 打包目录层次结构，类似命令行 tree 的效果，本题难度微提，请仔细阅读下面的注释，思考后做题。

# -*- coding: UTF-8 -*-
def dump_node(node, space, last):
    space = ''.join(space)
    if last:
        print(f"{space}└── {node}")
    else:
        print(f"{space}├── {node}")

def tree_project(node, depth, space):

    count = len(node)
    i = 0

    # 遍历一层下的节点
    while i < count:
        sub_node = node[i]

        # 获取子目录数据
        sub_dir = None
        if i+1 < len(node):
            if type(node[i+1]) == type([]):
                sub_dir = node[i+1]
                i += 1

        # 判断是否是本级别最后一个节点
        last = i == len(node) - 1

        # 打印当前节点
        dump_node(sub_node, space, last)

        # 如果含有子目录，则递归打印子目录结构
        if sub_dir is not None:
            # 在此实现计算当前层缩进空格的代码
            if depth == 0:
                next_space = ['']
            else:
                next_space = [*space]
                if not last:
                    next_space.append('|   ')
                else:
                    next_space.append('    ')
            tree_project(sub_dir, depth+1, next_space)

        i += 1


def test():
    project_files = [
        "packaging_tutorial",
        [
            "LICENSE",
            "pyproject.toml",
            "README.md",
            "setup.cfg",
            "src",
            [
                "example_package_1",
                [
                    "__init__.py",
                    "example_1.py"
                ],
                "example_package_2",
                [
                    "__init__.py",
                    "example_2.py"
                ],
            ],
            "tests/"
        ]
    ]

    print()
    print("# 介绍一下 Python 打包")
    print("* Python 打包教程：https://packaging.python.org/tutorials/packaging-projects/")
    print("* 一个典型 Python 包的目录结构如下：")
    print()
    tree_project(project_files, 0, [''])
    print()

if __name__ == '__main__':
    test()