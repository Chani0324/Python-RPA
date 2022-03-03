import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(100, 100) # 지정한 위치로 마우스 이동. 왼쪽상단이 0, 0
# pyautogui.moveTo(100, 200, duration=5) # duration으로 지정한 시간(s) 동안 이동

# 상대 좌표로 마우스 이동(현재 커서가 있는 위치로부터)
print(pyautogui.position()) # 현재 마우스가 있는 위치
pyautogui.move(100, 100)
pyautogui.move(100, 100)
print(pyautogui.position()) 

p = pyautogui.position()
print(p.x, p.y)