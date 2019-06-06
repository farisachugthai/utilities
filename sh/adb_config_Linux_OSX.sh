#!/bin/bash
# adb configuration script

PATH="$PATH:/bin:/sbin:/usr/sbin"
ANDROID_HOME=~/.android
ANDROID_CONFIG=~/.android/adb_usb.ini

CUST_VID="0x2a70"
if [ -e $ANDROID_HOME ] ; then
   echo "android home is exist!"
else
   echo "creat android home!"
   mkdir $ANDROID_HOME
fi
grep $CUST_VID $ANDROID_CONFIG 2>/dev/null
if [ $? -eq 0 ] ; then
   echo VID $CUST_VID is already configured..
   echo "adb should be OK!"
   exit 0
else
   echo config adb ...
   echo $CUST_VID >> $ANDROID_CONFIG
fi
adb kill-server
if [ $? -eq 0 ] ; then
  echo "OK! You can use adb now!"
  exit 0
else
   echo "try sudo exec adb.."
   sudo adb kill-server
   if [ $? -eq 0 ] ; then
       echo "OK! You can use adb now!"
       exit 0
   else
       echo "Please do command \"adb kill-server\""
   fi
fi
exit 0
