import pyautogui
import time

try:
    while True:
        pyautogui.click()  # 왼쪽 마우스 버튼 클릭
        time.sleep(15)  # 15초 대기
except KeyboardInterrupt:
    print("프로그램이 종료되었습니다.")
