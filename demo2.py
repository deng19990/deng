#定位元素
from selenium import webdriver
import time
drover = webdriver.Chrome()
drover.maximize_window()
drover.get("https://www.douyu.com")
drover.find_element_by_xpath('//*[@id="lazyModule3"]/div[2]/div[1]/h2/a').click()
time.sleep(3)
drover.window_handles
drover.switch_to.window(drover.window_handles[1])

while True:
    try:
        a=drover.find_element_by_class_name('dy-Pagination-item-custom').click()
        time.sleep(5)
    except Exception as a:
        break
drover.close()
drover.find_element_by_xpath('//*[@id="listAll"]/div[2]/div/ul/li[9]/span').click()
time.sleep(3)
drover.close()

