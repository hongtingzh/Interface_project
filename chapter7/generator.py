# 数据类（构造常用数据类型、UUID、文本、词组、文件链接、文件路径）
# 安全类（构造操作系统信息、HASH加密、密码）
# 信息类（构造个人信息数据和表单信息数据：姓名、地址、电话、工作、证件号、银行卡、公司）
# 网络类（构造IP MAC HTTP的客户端类型和文件类型、反反爬）


from faker import Factory


fake = Factory.create('zh_CN')


def random_python_data():
    return fake.pystr(), \
           fake.pyint(), \
           fake.pyfloat(), \
           fake.pybool(), \
           fake.pylist(nb_elements=2), \
           fake.pytuple(nb_elements=2), \
           fake.pydict(nb_elements=2)


def random_uuid():
    return fake.uuid4()


def random_text():
    return fake.text()


def random_word():
    return fake.word(), fake.words()


def random_image_url():
    return fake.image_url()


def random_file_path():
    return fake.file_path()


def random_os_info(os_type: str = 'win'):
    if os_type == 'win':
        return fake.windows_platform_token() + ' ' + fake.linux_processor()
    if os_type == 'linux':
        return fake.linux_processor()
    if os_type == 'mac':
        return fake.mac_platform_token()
    if os_type == 'ios':
        return fake.ios_platform_token()
    if os_type == 'android':
        return fake.android_platform_token()
    return None


def random_hash(raw_output: bool = False):
    return {'md5': fake.md5(raw_output), 'sha1': fake.sha1(raw_output), 'sha256': fake.sha256(raw_output)}


def random_password(length: int = 6,
                    special_chars: bool = False,
                    digits: bool = True,
                    upper_case: bool = False,
                    lower_case: bool = True):
    return fake.password(length=length,
                         special_chars=special_chars,
                         digits=digits,
                         upper_case=upper_case,
                         lower_case=lower_case
                         )


print(random_password())
