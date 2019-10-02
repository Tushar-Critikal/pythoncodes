import pyautogui, time
time.sleep(10)
pyautogui.click()    # click to put drawing program in focus
distance = 400
while distance > 0:
       pyautogui.dragRel(distance, 0, duration=0.2)   # move right
       distance = distance - 8
       pyautogui.dragRel(0, distance, duration=0.1)   # move down
       pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
       distance = distance - 8
       pyautogui.dragRel(0, -distance, duration=0.1)  # move up

