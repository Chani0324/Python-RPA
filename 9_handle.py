from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath("//*[@id='main']/div[2]/a").click()

handles = browser.window_handles # 모든 handle 정보
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)
    print(browser.title)
    print()

# 새로 이동된 브라우저에서 자동화 작업 수행 ..

# 이전 핸들로 돌아오기
browser.switch_to.window(handles[0])

# browser.close()

time.sleep(5)