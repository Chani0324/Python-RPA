from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"download.default_directory":"C:\\Users\\YSJ\\Desktop\\RPA"})

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame("iframeResult")

# download link click
elem = browser.find_element_by_xpath("/html/body/p[2]/a/img")
elem.click()

time.sleep(5)