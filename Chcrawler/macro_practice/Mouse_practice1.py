import win32api, win32con, win32gui
import pyautogui
import sys
import io
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



# win32api 연습
# pos = win32api.GetCursorPos()
# win32api.SetCursor(100, 200)
# print(pos)

# pyautogui 연습
# chrome_button = {
#     'top_left' : {'x' : 0, 'y' : 27},
#     'bottom_right' : {'x' : 64, 'y' : 89}
# }
# x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
# y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
# pyautogui.moveTo(x, y, duration = 2) # ~동안에 = 2초간 x와 y의 좌표로 이동

# a = pyautogui.size()
# print(a)

# try:
#     while True:
#         x, y = pyautogui.position()
#         print('x : {}, y : {}'.format(x,y))
#
# except KeyboardInterrupt:
#     print('프로그램을 종료합니다.')

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
#         print('\b' * (len(positionStr) + 2), sys.stdout.flush())
#
# except KeyboardInterrupt:
#     print('\n')

# 마우스 duration 5초로 이동
# pyautogui.moveTo(0,0,5)

# 내 마우스 좌표 실시간으로 찍기
# while True:
#     x, y = pyautogui.position()
#     print('x좌표 : %s, y좌표 : %s' % (x , y))

# 마우스 위치 텍스트 파일에 기록
# with open('mouse.txt', 'a') as file:
#     while True:
#         pos = pyautogui.position()
#         file.write(f'{pos[0]}, {pos[1]}\n')
#         sleep(.16)

driver = webdriver.Chrome()
action = ActionChains(driver)
action.send_keys('aaaa').perform()
action.reset_actions()

# 서버 시간에 맞춰 클릭해주는 매크로
# endhope = False
# while not endhope:
#     tim = dt.datetime.now()
#     if tim.second>=59 and tim.microsecond>600000:
#         pyautogui.click(1301,722)
#         endhope=True
#         print(tim)
#     else:
#         time.sleep(0.1)
#         print(tim)

        
