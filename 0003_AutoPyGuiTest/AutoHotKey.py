# module 불러오기
import pyautogui
import keyboard
import time

# 간단한 키보드 매크로
def simple_macro():
    time.sleep(1)
    pyautogui.write('This is a simple macro executed by Python.', interval=0.05)
    pyautogui.press('enter')

# 복잡한 매크로
def complex_macro():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(100, 100)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

def pass_macro():
    time.sleep(0.1)
    pyautogui.write('tjdruranswp1!', interval = 0.01)

def tab_macro():
    time.sleep(0.1)
    pyautogui.write('jjeek.hwang', interval = 0.01)
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.1)
    pyautogui.write('tjdruranswp1!', interval = 0.01)
    time.sleep(0.1)
    pyautogui.hotkey('enter')

# 특정 키를 눌렀을 때 매크로 실행
keyboard.add_hotkey('ctrl+shift+s', simple_macro)
keyboard.add_hotkey('ctrl+shift+c', complex_macro)
keyboard.add_hotkey('ctrl+shift+j', pass_macro)
keyboard.add_hotkey('ctrl+shift+p', tab_macro)


print("Press Ctrl+Shift+S to run the simple macro.")
print("Press Ctrl+Shift+C to run the complex macro.")
print("Press Ctrl+Shift+J to run the pass macro.")
print("Press Ctrl+Shift+P to run the pass macro.")

# esc 키를 누를 때까지 프로그램 실행
keyboard.wait('esc')