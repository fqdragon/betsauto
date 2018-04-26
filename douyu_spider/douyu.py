# -*- coding: utf-8 -*-

from douyu_spider.chromedriver import ChromeDriver
import time

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

def test(url):
    try:
        testd = ChromeDriver()
        testd.get(url)
        testd.implicitly_wait(30)
        time.sleep(30)
        btn = testd.find_element_by_xpath('//div[contains(@class,"guess-game-btn")]')
        btn.click()
        bets = testd.find_elements_by_xpath('//div[contains(@class,"guess-game-box")]')
        for bet in bets:
            print(bet.text)
    except Exception as e:
        print("test:", e)
    finally:
        testd.quit()


def betAct(bet):
    rl = 1
    assets = bet.find_element_by_xpath('//div/em[contains(@class,"fishBall_NUM")]')
    print(assets.text)
    left_element = bet.find_element_by_xpath(
        '//div[@class="guess-game-box-container"]/a[@class="item item-left"]')
    right_element = bet.find_element_by_xpath(
        '//div[@class="guess-game-box-container"]/a[@class="item item-right"]')
    rw_left = left_element.get_attribute('data-loss')
    print(rw_left)
    rw_right = right_element.get_attribute('data-loss')
    print(rw_right)

def goBet(href):
    roomDriver = ChromeDriver()
    try:
        roomDriver.get(href)
        roomDriver.implicitly_wait(30)
        betBtn = roomDriver.find_element_by_xpath('//div[contains(@class,"guess-game-btn")]')
        betBtn.click()
        bets = roomDriver.find_elements_by_xpath('//div[contains(@class,"guess-game-box")]')
        for bet in bets:
            betAct(bet)
    except Exception as e:
        print("goBet:", e)
    finally:
            roomDriver.quit()



def getBetroom(url):
    driver = ChromeDriver()
    betRooms = []
    try:
        driver.get(url)#访问页面
        driver.implicitly_wait(3)#等待一定时间，让js脚本加载完毕
        rooms = driver.find_elements_by_xpath('//div/ul[@id="live-list-contentbox"]/li')
        for room in rooms:
            try:#如果没开竞猜，会出现找不到元素的异常
                if room.find_element_by_xpath('a/span/i[@class="icon_quiz"]'):
                    href = room.find_element_by_xpath('a').get_attribute("href")
                    betRooms.append(href)
            except Exception:
                pass
            if len(betRooms) >= 3:
                break
        #竞猜：//div/ul[@id='live-list-contentbox']/li/a/span/i[@class='icon_quiz']
        #房间号
    except Exception as e:
        print("getBetroomm:", e)
    finally:
        driver.quit()
        return betRooms


if __name__ == '__main__':
    try:
        betRooms = []
        url = "https://www.douyu.com/directory/game/DOTA2"
        # betRooms = getBetroom(url)
        # for room in betRooms:
        #     goBet(room)
        goBet("https://www.douyu.com/9999")
        # test("https://www.douyu.com/9999")
    except Exception as e:
        print("main():", e)
