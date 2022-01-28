# 项目地址
# 项目包和文件夹路径
# 测试组件
from os.path import join, dirname
import logging

# --------------------项目地址--------------------
# 项目一地址
PROJECT_ZenTao_URL = 'http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'

# 项目二地址
PROJECT_QQ_URL = ''

# 项目三地址
PROJECT_Demo_URL = ''
# --------------------项目地址--------------------

# --------------------项目包和文件夹路径--------------------
# 项目根目录
BASE_PATH = dirname(__file__)

# 浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, 'drivers/chromedriver.exe')
FIREFOX_DRIVER_PATH = join(BASE_PATH, '')
IE_DRIVER_PATH = join(BASE_PATH, '')
EDGE_DRIVER_PATH = join(BASE_PATH, 'drivers/msedgedriver.exe')
OPERA_DRIVER_PATH = join(BASE_PATH, '')

# 项目模块路径
# 模块1路径
CHAPTER_1_PATH = join(BASE_PATH, 'chapter3')

# 模块2路径
CHAPTER_2_PATH = join(BASE_PATH, 'chapter4')

# 元素配置文件的根目录
ELEMENTS_YAML_FILE_PATH = join(BASE_PATH, 'chapter5/page')
# --------------------项目包和文件夹路径--------------------

# --------------------测试套件--------------------
# 流程1相关测试套件
SUIT_MODULE_1 = ['test_module_1.py', 'test_module_2.py']

# 流程2相关测试套件
SUIT_MODULE_2 = ['test_module_3.py', 'test_module_4.py']

# 主测试套件
SUIT = SUIT_MODULE_1 + SUIT_MODULE_2
# --------------------测试套件--------------------

# --------------------浏览器对象属性--------------------
# 浏览器启动参数配置
# 浏览器尺寸
WINDOWS_SIZE = (1024, 768)

# 隐式等待时间
IMP_TIME = 30

# 页面加载时间
PAGE_LOAD_TIME = 20

# js执行时间
SCRIPT_TIME_OUT = 20

# 无头化
HEADLESS = True

# ----------------chrome浏览器属性----------------
# chrome浏览器操作开关
CHROME_OPTION_MARK = True

# chrome浏览器启动参数开关
CHROME_METHOD_MARK = True

# chrome浏览器实质性质启动参数
CHROME_EXPERIMENTAL = {
        'excludeSwitches': ['enable-automation'],     # 不会提示‘正受到自动测试软件的控制’
        # 'mobileEmulation': {'deviceName': 'iPhone 6'}   # 以移动模拟的形式打开某个网页，一般web用不到，在做H5需要在网页实现的时候就必须要添加
    }

CHROME_PRE = {'credentials_enable_service': False,
              'profile.password_manager_enabled': False
              }

# chrome浏览器窗口大小启动参数
CHROME_WINDOWS_SIZE = (1920, 900)

# chrome浏览器隐式等待时间
CHROME_IMP_TIME = 30

# chrome浏览器页面加载时间
CHROME_PAGE_LOAD_TIME = 20

# chrome浏览器执行时间
CHROME_SCRIPT_TIME_OUT = 20

# chrome浏览器无头化
CHROME_HEADLESS = False

# chrome浏览器启动最大化参数
CHROME_START_MAX = '--start-maximized'  # 对应的是option的启动参数
# ----------------chrome浏览器属性----------------

# ----------------ie浏览器属性----------------
# ----------------ie浏览器属性----------------
# --------------------浏览器对象属性--------------------

# --------------------YAML元素配置文件--------------------
YAML_ELEMENT = {
    'cp': join(ELEMENTS_YAML_FILE_PATH, 'common_login_page.yml'),
    'sp': join(ELEMENTS_YAML_FILE_PATH, 'search_page.yml')
}
# --------------------YAML元素配置文件--------------------

# --------------------selenium支持的定位类型--------------------
from selenium.webdriver.common.by import By
BY_RULES = (
    'id',
    'xpath',
    'link text',
    'partial link text',
    'name',
    'tag name',
    'class name',
    'css selector'
)
# --------------------selenium支持的定位类型--------------------

# --------------------日志文件相关配置--------------------
# 日志日期格式
LOG_FORMATTER = ('%(asctime)s-%(name)s-%(levelname)s-%(status)s: %(message)s',
                 '%H:%M:%S')

# 日志文件名
LOG_NAME = f'demo_log'

# 日志文件路径
LOG_FILE = join(BASE_PATH, 'chapter6/demo.log')

# 日志记录等级
LOG_LEVEL = logging.DEBUG
# --------------------日志文件相关配置--------------------

# --------------------邮件相关配置--------------------
# 发件人邮箱
sender = 'hongtingzhang@qq.com'

# 收件人邮箱
receiver = ['1462367817@qq.com', 'hongting@faisco.biz']

# 邮件title
title = '测试报告'

server = 'smtp.qq.com'

# 发送邮件的授权码
auth_code = 'hivwbxkuautfifji'
# --------------------邮件相关配置--------------------

