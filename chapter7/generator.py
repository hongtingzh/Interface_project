# 数据类（构造常用数据类型、UUID、文本、词组、文件链接、文件路径）
# 安全类（构造操作系统信息、HASH加密、密码）
# 信息类（构造个人信息数据和表单信息数据：姓名、地址、电话、工作、证件号、银行卡、公司）
# 网络类（构造IP MAC HTTP的客户端类型和文件类型、反反爬）


from faker import Factory


fake = Factory.create('zh_CN')


def random_python_data():
    return fake.pystr()
