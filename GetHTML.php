<?php
// this pgm uses another python pgm to fetch a web page and render in pure html, then displays
function geturl($url)
{
$base=$_SERVER['DOCUMENT_ROOT'];
$cmd='cd '.$base.'shares/data && /usr/bin/python3 /home/bruce/SW/python/GetPage/GetPage.py "'.$url.'"';
// DEBUG print("<br>CMD=".$cmd);
ob_start();
passthru($cmd);
$html = ob_get_clean(); 
return $html;
}
?>