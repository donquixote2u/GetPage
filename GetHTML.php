<?php
// this pgm uses another python pgm to fetch a web page and render in pure html, then displays
function geturl($url)
{
$base=$_SERVER['DOCUMENT_ROOT'];
// GCE version; $cmd='sudo  /usr/bin/python '.$base.'python/GetPage/GetPage.py '.$url; 
$cmd='python3 '.$base.'/python/GetPage/GetPage.py '.$url; 
//DEBUG error_log("cmd=".$cmd,3,"/tmp/err.txt");
ob_start();
passthru($cmd);
$html = ob_get_clean(); 
return $html;
}
if(__FILE__ ==$_SERVER['SCRIPT_FILENAME'])   // if this script called directly from server,
    {print(geturl($_GET['url']));}					//  display page from url passed in this request 
?>
