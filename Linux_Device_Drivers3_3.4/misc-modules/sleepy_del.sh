#!/bin/bash

rm -f /dev/sleepy 
rmmod sleepy || exit 1 
