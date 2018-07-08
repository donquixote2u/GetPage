# GetPage
Uses Python to render any given webpage (which may be generated to any extent with javascript), into its final html form (e.g. for webscraping) using qtwebengine

python prerequisites;  
pyvirtualdisplay (for running in batch mode) 
pyqt5 
pyqt5.qtwebengine  (separate module in Debian and Ubuntu)

Ubuntu may also require xvfb installed.

FlaskRender is a flask framework for GetPage for use as a web service

GetPageWk is an earlier webkit version of GetPage;  webengine replaced webkit in Chrome, 
but webkit survives as a fork.

GETHTML.php is an example of using GetPage in php. just call webpage with url as argument e.g.
http://localhost/GetHTML.php?url=someurl.com

GetPage.sh is an example of a cgi shell script calling python  (put in your webserver cgi folder)

EXAMPLE USAGE: 
batch mode; python3 GetPage.py "http://www.mypage.php" > mypage.html

flask web service; 
start web service: python3 FlaskRender.py  
send request url to web service with Render argument + url: http://localhost:5000/Render?url=http://mywebpage.com




