# GetPage
python page render into html

example: python3 GetPage.py "http://www.mypage.php" > mypage.html

this uses the qt 5 webkit to render pages that may have a large degree of javascript rendering of content.

developed in a Debian environment where prerequisites were :
PyQt5
PyQt5-WebKit

todo;
investigate webengine-based equivalent
The Chromium browser now uses webengine as its core;
webkit has been forked as a parallel development, but support is uncertain.


