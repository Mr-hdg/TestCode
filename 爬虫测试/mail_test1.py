import time
from selenium import webdriver


def mail_test(ip):

    # 用谷歌浏览器开启
    driver = webdriver.Chrome()
    # 进入指定QQ企业邮箱
    driver.get(ip)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[4]/a').click()
    time.sleep(1)
    # 清空帐号框内的内容
    driver.find_element_by_xpath('//*[@id="inputuin"]').clear()
    time.sleep(1)
    # 输入指定帐号 user="abc"自己定义
    driver.find_element_by_xpath('//*[@id="inputuin"]').send_keys(user)
    time.sleep(1)
    # 输入密码 pwd="123"
    driver.find_element_by_xpath('//*[@id="pp"]').send_keys(pwd)
    time.sleep(2)
    # 点击登陆
    driver.find_element_by_xpath('//*[@id="btlogin"]').click()

    return driver

def mail_fa2shou(web):
    time.sleep(1)
    # 点击左侧发件箱
    web.find_element_by_xpath('//*[@id="folder_3"]').click()
    time.sleep(1)
    # 切换次页面
    web.switch_to.frame("mainFrame")
    # 下面的函数是判断收件箱是否还有邮件，返回True或False
    res = mail_count(web)
    while res:
        time.sleep(1)
        # 选择当页所有邮件
        web.find_element_by_xpath('//*[@id="frm"]/table/tbody/tr/td[1]/input').click()
        time.sleep(1)
        # 打开“移动至”下拉框
        web.find_element_by_xpath('//*[@id="selmContainer"]/div').click()
        time.sleep(1)
        # 选择收件箱
        web.find_element_by_xpath('//*[@id="select_s__menuitem_fid_1"]').click()
        time.sleep(1)
        # 重新判断收件箱是否还有邮件，返回True或False
        res = mail_count(web)
    # 退出浏览器
    web.quit()

def mail_count(web):
    # 进入指定位置
    table = web.find_element_by_xpath('//*[@id="frm"]/div[3]')
    # 获取指定位置所有关于“table”的数据
    t_rows = table.find_elements_by_tag_name("table")
    # 判断t_rows是否为空
    if len(t_rows) > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    ip = "https://exmail.qq.com/login"
    user = "zhouw@windit.com.cn"
    pwd = "Zhou2019"

    wb = mail_test(ip)
    mail_fa2shou(wb)