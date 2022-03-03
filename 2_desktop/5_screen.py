import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# 마우스 포지션에 따른 RGB값 비교 가능
# pyautogui.mouseInfo()
# 41,23 64,170,242 #40AAF2
# pixel = pyautogui.pixel(41, 23)
# print(pixel)
print(pyautogui.pixelMatchesColor(41, 23, (64, 170, 242)))


