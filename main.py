import webbrowser
import pyautogui as pg
url=input("enter your url:")
url=url[:12]+'ss'+url[12:]
webbrowser.open(url)
pg.sleep(4)
pg.leftClick(938,556,2)



