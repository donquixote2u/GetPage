## webkit scraper vsn 4 24/9/17  - works in cli mode, redirect output to file
## example: python3 GetPage.py "http://www.mypage.php" > mypage.html
## if using python2 uncomment print with encoding  (11/2/18 utf-8 encoding explicit)
# -*- coding: utf-8 -*-
import sys
import codecs
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Render(QWebEngineView):
        def __init__(self):
                self.batch=False
                self.app = QApplication(sys.argv)
                self.html = None
                QWebEngineView.__init__(self)
                self.loadFinished.connect(self._loadFinished)

        def _loadFinished(self, result):
            # html render is async,  controls close
            self.page().toHtml(self.callable)

        def callable(self, data):
            # this is only called on html output completion    
            self.html = data
            if(self.batch): ## if not batch, html is returned to caller
              print(self.html.encode("utf-8","ignore")) # 11/2/18 utf-8 coding explicit
              # uncomment line below if python2 
              # print(unicode(self.html).encode('utf-8'))  
              sys.exit()
            else: 
              self.app.quit()

if __name__ == '__main__':
        ## set up virtual display to receive webengine output if run in batch mode
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
        #app = QApplication(sys.argv)
        #url=app.arguments()[1]
        #if(url):	## get url from passed args
        view = Render()
        view.batch=True
        view.load(QUrl(view.app.arguments()[1]))
        view.app.exec_()
        
         


            







