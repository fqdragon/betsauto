# -*- coding: utf-8 -*-

from chromedriver import ChromeDriver



# def get_price(driver,url):
# 	try:
# 		driver.get(url)
# 		time.sleep(2)
# 		price = driver.find_element_by_xpath("//div[@id='arrowud']/strong[@id='price9']").text
# 		return (price)
# 	except Exception,e:
# 		print "get_price:"+str(e)

def loginDouyu(driver, url):
    try:
        driver.get(url)
        # 输入用户名
        username = driver.find_element_by_name('user')
        username.send_keys('学号')

        # 输入密码
        password = driver.find_element_by_name('pwd')
        password.send_keys('密码')

        # 选择“学生”单选按钮
        student = driver.find_element_by_xpath('//input[@value="student"]')
        student.click()

        # 点击“登录”按钮
        login_button = driver.find_element_by_name('btn')
        login_button.submit()
    except Exception:
        print("loginDouyu")

def getBetroom(driver, url):
    try:
        driver.get(url)#访问页面
        driver.implicitly_wait(3)#等待一定时间，让js脚本加载完毕
    except Exception:
        print("getBetroomm")


if __name__ == '__main__':
    try:
        myDriver = ChromeDriver()
    except Exception:
        print("main():")