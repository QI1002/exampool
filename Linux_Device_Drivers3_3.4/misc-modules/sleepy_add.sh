#!/bin/bash
module="sleepy"   
device="sleepy"  
mode="666"

# invoke insmod with all arguments we got  
# and use a pathname, as newer modutils don't look in . by default

insmod ./$module.ko $* || exit 1

# remove stale nodes  
rm -f /dev/${device}   

major=$(awk "\$2 == \"$module\" {print \$1}" /proc/devices)
mknod /dev/${device} c $major 0
chmod ${mode} /dev/sleepy

# use these commands to test 
# echo 123 > /dev/sleepy
# cat /dev/sleepy

