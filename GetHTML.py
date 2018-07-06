#!/usr/bin/python
## WIP - not tested!
## get web page using GetPage.py;  this is a wrapper intended for apache web server use
# Turn on debug mode.
from GetPage import *
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()
url="https://www.xe.com/currency/nzd-new-zealand-dollar"
from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
with Display(visible=0, size=(800, 600)) as display:  ## with breaks down display on exit
          view = Render()
          view.batch=True
          view.load(QUrl(url)) ## get url from passed args
          view.app.exec_()
          display.sendstop()
          print(view.html)
quit()
