# -*- coding: utf-8 -*-

from .chromedriver import ChromeDriver


# def get_price(driver,url):
# 	try:
# 		driver.get(url)
# 		time.sleep(2)
# 		price = driver.find_element_by_xpath("//div[@id='arrowud']/strong[@id='price9']").text
# 		return (price)
# 	except Exception,e:
# 		print "get_price:"+str(e)
if __name__ == '__main__':
    try:
        myDriver = ChromeDriver()
    except Exception:
        print("main():")