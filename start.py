# 测试套件 -- 包含待测的模块、类、测试方法
# 测试加载器 -- 决定测试模块、测试类、测试方法的加载
# 测试运行器 -- 记录测试过程、测试测试结果
import unittest
from os.path import join, dirname
from chapter4.case import tests
from HTMLTestRunner import HTMLTestRunner
from chapter7.mail import Email

# CASE_PATH = join(dirname(__file__), 'chapter4/case')
#
# # 测试套件初始化，测试加载器初始化
# suit = unittest.TestSuite()
# loader = unittest.TestLoader()
#
# # 测试加载器发现测试对象
# for test in tests:
#     # test_suit = loader.discover(start_dir=CASE_PATH, pattern='*module1*.py')
#     test_suit = loader.discover(start_dir=CASE_PATH, pattern=test)
#     # 测试对象加入测试套件
#     suit.addTest(test_suit)
#
# # 测试运行器初始化
# # with open('./report.txt', 'w') as fp:
# #     runner = unittest.TextTestRunner(fp, verbosity=2)
# #
# #     # 运行测试
# #     runner.run(suit)
#
# with open('./report.html', 'w') as fp:
#     runner = HTMLTestRunner(fp, verbosity=2, title='test')
#     runner.run(suit)


Email(message='start.py里面的信息', attachment_file=r'D:\Tools\git\workspace\Interface_project\report.html').send()
