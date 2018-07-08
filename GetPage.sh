#!/bin/bash
## intended to run python script as cgi under apache2 webserver (put in cgi-bin folder)
echo QUERYSTRING=$QUERY_STRING
ARG1=`echo "$QUERY_STRING" | awk -F"[=&]" '{printf $2 }'`
echo ARG1=$ARG1
/usr/bin/python /home/bruce/SW/websites/python/GetPage/GetPage.py $ARG1


