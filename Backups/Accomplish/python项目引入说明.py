"""
文件结构

根目录

root

    package1

        __init__.py
            package1 初始化

        1_file1.py
            from .1_file2 import file2 as 1_2
            from package2.2_file2 import file2 as 2_2

        1_file2.py
            from .1_file1 import file1 as 1_1
            from package2.2_file1 import file1 as 2_1

    package2
        2_file1.py
        2_file2.py

    config.py  参数文件

    run.py     只能运行文件   --  项目只能运行这个



"""