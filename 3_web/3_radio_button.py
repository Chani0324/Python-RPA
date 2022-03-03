from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")
browser.switch_to.frame("iframeResult") # frame 전환

elem = browser.find_element_by_xpath("//*[@id='html']")

# 체크가 안 되어 있으면 선택하기
if elem.is_selected() == False:
    elem.click()
else:
    print("선택 되어 있음")

time.sleep(3)

if elem.is_selected() == False:
    elem.click()
else:
    print("선택 되어 있음")

