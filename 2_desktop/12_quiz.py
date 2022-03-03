import pyautogui
import time
import pyperclip
import sys

# 그림판 실행
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

# 텍스트 상자 찾아서 클릭 후 그림판 영역 선택 -> 글자입력
pyautogui.sleep(2)
mspaint = pyautogui.getWindowsWithTitle("제목 없음")[0]
# mspaint.active()
mspaint.maximize()


def find_target(img_file, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence=0.8)
        end = time.time()
        if end - start > timeout:
            sys.exit()
        else:
            break
    return target

def my_click(img_file, timeout):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        sys.exit()

my_click("mspaint_text.png", 50)
pyautogui.move(0, 200)
pyautogui.click()
pyperclip.copy("참 잘했어요.")
pyautogui.hotkey("ctrl", "v")

# 5초 대기 후 프로그램 종료(저장하지 않음 선택)
pyautogui.sleep(5)
pyautogui.hotkey("alt", "f4")
pyautogui.sleep(1)
my_click("mspaint_not_save.png", 100)
