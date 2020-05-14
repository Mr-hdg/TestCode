import time
import os
from selenium import webdriver


def mail_test(ip, user, pwd):

    # 获取谷歌插件的位置
    chr_path = os.path.join(os.getcwd(),"chromedriver")
    # 用谷歌浏览器开启
    driver = webdriver.Chrome(executable_path=chr_path)
    # 进入指定QQ企业邮箱
    driver.get(ip)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[3]/a[1]').click()
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

def mail_all(web):
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="logotips"]/div/div/span[3]/a[2]').click()

    time.sleep(1)
    # 切换次页面
    web.switch_to.frame("mainFrame")
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="web_set"]/div[1]/div[1]/div/div/div[10]/a').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="poprecent"]/option[1]').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="sendbtn"]').click()
    time.sleep(1)
    web.switch_to.parent_frame()

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
    # 写上自己的企业邮箱帐号
    # user = "wangjk@windit.com.cn"
    # 写上自己的密码
    # pwd = "Wang2019"

    user = input("请输入邮箱：")
    pwd = input("密码：")
    wb = mail_test(ip, user, pwd)
    mail_all(wb)
    mail_fa2shou(wb)