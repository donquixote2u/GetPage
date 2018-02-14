## Pywebtask :receives task request as GET, returns task result
import os
from GetPage import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'No service identified'

@app.route('/Render')
def api_render():
        url=request.args.get('url')
        if(url):
          from pyvirtualdisplay import Display
          display = Display(visible=0, size=(800, 600))
          display.start()           ## webengine needs a display so create dummy
          view = Render()       ## go get rendered web page using url
          view.load(QUrl(url))
          view.app.exec()       ## start qt processing incl monitor for completion
          display.stop()
          return view.html
        else: 
          return "No Url Supplied"  
          
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    ## uncomment for debug
    ##if port == 5000:
    ##     app.debug = True
    # accept rq on external interface
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=port)
