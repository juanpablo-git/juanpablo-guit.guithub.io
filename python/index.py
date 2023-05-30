import pyautogui as py
import time

py.press("win")
time.sleep(1)
py.write("firefox")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.hotkey('ctrl', 'l')
time.sleep(1)
py.write("https://mail.google.com/mail/u/0/#search/cart%C3%B5es+caixa")
time.sleep(1)
py.press("enter")
time.sleep(5)
py.moveTo(600, 340)  
time.sleep(1)
py.click()
time.sleep(1)
py.moveTo(626,428)  
time.sleep(2)
py.click()
py.write("")
time.sleep(2)
py.press("enter")
time.sleep(5)
print(py.position())
py.moveTo(1288,144)  
py.click()
time.sleep(2)
py.press("enter")
time.sleep(2)
py.press("enter")
time.sleep(1)
py.hotkey('ctrl', 't')
time.sleep(1)
py.hotkey('ctrl', 'l')
py.write("web.whatsapp.com/")
time.sleep(1)
py.press("enter")






