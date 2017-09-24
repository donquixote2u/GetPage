# GetPage
Uses Python to render any given webpage (which may be generated to any extent with javascript), into its final html form (e.g. for webscraping) using qtwebengine

Prerequisites;  Pyvirtualdisplay (for running in batch mode), PyQt5, PyQt5.WebEngine  (separate module in Debian and Ubuntu)
Ubuntu may also require xvfb installed.

FlaskRender is a flask framework for GetPage for use as a web serviced

GetPageWk is an earlier webkit version of GetPage;  webengine replaced webkit in Chrome, 
but webkit survives as a fork.

EXAMPLE USAGE: 
batch mode; python3 GetPage.py "http://www.mypage.php" > mypage.html

web service; 
start web service: python3 FlaskRender.py  
send request url to web service with Render argument + url: http://localhost:5000/Render?url=http://mywebpage.com



