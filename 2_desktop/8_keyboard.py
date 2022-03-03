import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]   
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Nadocoding", interval=0.5)
# pyautogui.write("나도 코딩")

# pyautogui.write(["t", "e", "s", "t", "left", "left", "left", "l", "a", "enter"], interval=0.25)

# 특수 문자
# shift
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 (Het key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "a") # ctrl 누름> a 누름 > a 뗌 > ctrl 뗌

# 문장을 클립보드에 저장
import pyperclip
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")


# 자동화 프로그램 종료
# ctrl + alt + del