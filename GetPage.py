## webkit scraper vsn 2 9/9/17  - works in cli mode, redirect output to file
## example: python3 GetPage.py "http://www.mypage.php" > mypage.html
import sys
from pyvirtualdisplay import Display
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import QApplication
from PyQt5.QtCore import QUrl
# from PyQt5.QtWebKit import QWebView
from PyQt5.QtWebKitWidgets import *

class Browser(QWebView):

    def __init__(self):
        QWebView.__init__(self)
        self.loadFinished.connect(self._result_available)

    def _result_available(self, ok):
       frame = self.page().mainFrame()
       # python<3 # self.html=unicode(frame.toHtml()).encode('utf-8')
       print(self.html=frame.toHtml())
       sys.exit()


if __name__ == '__main__':
	display = Display(visible=0, size=(800, 600))
	display.start()
	app = QApplication(sys.argv)
	if(url=app.arguments([1])):
		view = Browser()
		view.load(QUrl(url))
		app.exec_()