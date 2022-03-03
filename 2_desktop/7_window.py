import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보를 가져옴
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows(): # 모든 윈도우 가져오기
#     print(w)

# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize()

w.restore()

w.close()