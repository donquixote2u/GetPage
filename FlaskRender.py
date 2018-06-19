## web server; receives url request as GET, returns web page fully rendered into html
import os
from GetPage import *
from flask import Flask, request
from pyvirtualdisplay import Display

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'No service identified'

@app.route('/Render')
def api_render():
        url=request.args.get('url')
        if(url):
             view = Render()       ## go get rendered web page using url
             view.load(QUrl(url))
             view.app.exec_()       ## start qt processing incl monitor for completion
             return view.html
        else: 
          return "No Url Supplied"  
          
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # accept rq on external interface
    with Display(visible=0, size=(800, 600)) as display:  ## with breaks down display on exit
      app.run(host='0.0.0.0', port=port) ## change interface address as required
      display.stop()
 
