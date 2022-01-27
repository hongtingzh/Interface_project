# 裸奔代码

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 启动浏览器
driver = webdriver.Chrome()
driver.maximize_window()


# 打开目标王章
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')

# 登录
sleep(1)
driver.find_element(By.ID, "account").send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys("Aaa123456")
driver.find_element(By.XPATH, '//*[@id="submit"]').click()

# 登录断言
sleep(1)
driver.switch_to.frame('appIframe-my')
home = driver.find_element(By.XPATH, '//*[@id="userNav"]/li[1]/a/div')
# perform是悬浮，perform前面是找到元素
ActionChains(driver).move_to_element(home).perform()
name = driver.find_element(By.XPATH, '//*[@id="userNav"]/li[1]/ul/li[1]/a/div[2]').text

if name == 'admin':
    print('pass')
else:
    print('fail')

# 检索bug单
driver.switch_to.default_content()
driver.find_element(By.ID, 'globalSearchInput').send_keys('001')
driver.find_element(By.XPATH, '//*[@id="globalSearchButton"]/i').click()
sleep(1)
driver.switch_to.frame('appIframe-qa')
# 检索bug单断言
if driver.find_element(By.XPATH, '//*[@id="mainMenu"]/div[1]/div[2]/span[1]').text == '1':
    print('pass')
else:
    print('fail')
sleep(3)
driver.quit()

