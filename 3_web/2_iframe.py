from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")
browser.switch_to.frame("iframeResult") # frame 전환

elem = browser.find_element_by_xpath("//*[@id='html']")
elem.click()

browser.switch_to.default_content() # 상위로 빠져나옴

elem = browser.find_element_by_xpath("//*[@id='html']")

time.sleep(5)

browser.quit()