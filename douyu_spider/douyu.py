# -*- coding: utf-8 -*-

from douyu_spider.chromedriver import ChromeDriver


# def loginDouyu(driver, url):
#     try:
#         driver.get(url)
#         # 输入用户名
#         username = driver.find_element_by_name('user')
#         username.send_keys('学号')
#
#         # 输入密码
#         password = driver.find_element_by_name('pwd')
#         password.send_keys('密码')
#
#         # 选择“学生”单选按钮
#         student = driver.find_element_by_xpath('//input[@value="student"]')
#         student.click()
#
#         # 点击“登录”按钮
#         login_button = driver.find_element_by_name('btn')
#         login_button.submit()
#     except Exception:
#         print("loginDouyu")

def getBetroom(driver, url):
    try:
        driver.get(url)#访问页面
        driver.implicitly_wait(3)#等待一定时间，让js脚本加载完毕
        rooms = driver.find_element_by_xpath('//div/ul[@id="live-list-contentbox"]/li')
        print(rooms)
        for room in rooms:
            if driver.find_element_by_xpath('./a/span/i[@class="icon_quiz"]'):
                href = driver.find_element_by_xpath('./a/@href')
                print(href)
        #竞猜：//div/ul[@id='live-list-contentbox']/li/a/span/i[@class='icon_quiz']
        #房间号
    except Exception:
        print("getBetroomm")
        driver.quit()


if __name__ == '__main__':
    try:
        url = "https://www.douyu.com/directory/game/DOTA2"
        myDriver = ChromeDriver()
        getBetroom(myDriver, url)
    except Exception:
        print("main():")