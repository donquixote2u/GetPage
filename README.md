# GetPage
Uses Python to render any given webpage (which may be generated to any extent with javascript), into its final html form (e.g. for webscraping) using qtwebengine

Prerequisites;  Pyvirtualdisplay (for running in batch mode), PyQt5, PyQt5.WebEngine  (separate module in Debian and Ubuntu)
Ubuntu may also require xvfb installed.

example: python3 GetPage2.py "http://www.mypage.php" > mypage.html

GetPageWk is an earlier webkit version of GetPage;  webengine replaced webkit in Chrome, 
but webkit survives as a fork.


