import pyautogui

pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write("paint")
pyautogui.sleep(1)
pyautogui.press("ENTER")
pyautogui.sleep(1)

pyautogui.moveTo(1022,409)
pyautogui.dragRel(200.0)
pyautogui.dragRel(0,200,duration=0.2)
pyautogui.dragRel(-200,0,duration=0.2)
pyautogui.dragRel(0,-200,duration=0.2)









