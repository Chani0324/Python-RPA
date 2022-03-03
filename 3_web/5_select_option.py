from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")
browser.switch_to.frame("iframeResult") # frame 전환

# elem = browser.find_element_by_xpath("//*[@id='cars']/option[4]")
# elem.click()

# 텍스트 값을 통해서 선택
# elem = browser.find_element_by_xpath("//*[@id='cars']/option[text()='Audi']")
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
elem = browser.find_element_by_xpath("//*[@id='cars']/option[contains(text(), 'Au')]")
elem.click()


while True:
    pass