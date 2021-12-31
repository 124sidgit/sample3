#THis program is to take screenshot
#import pyscreenshot and time module
import pyscreenshot
import time


time.sleep(5)
img=pyscreenshot.grab() # To capture the screen
img.show() # To display the captured screenshot
img.save("ss.png") # To save the screenshot