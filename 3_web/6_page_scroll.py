from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://shopping.naver.com/home/p/index.naver")

browser.find_element_by_xpath("//*[@id='autocompleteWrapper']/input[1]").send_keys("무선 마우스")

browser.find_element_by_xpath("//*[@id='autocompleteWrapper']/a[2]").click()

## 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 모니터 해상도만큼

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
# 현재 문서 높이를 가져와서 저장
interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height


while True:
    pass