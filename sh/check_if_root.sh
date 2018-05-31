#!/bin/bash
#Check if the user who ran the script is root

if [ "$UID" -ne "$ROOT_UID" ] 
then
   echo "Must be root to run the script."
   exit $E_NOTROOT
fi

## So i think I got that from the advanced bash scripting guide. here's stack overflow
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# alledgedly using double brackets and not quoting is better form. *shrugs*

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit
fi