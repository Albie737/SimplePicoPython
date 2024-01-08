#!/bin/bash

cd /
sleep 0.2s
cd Home
sleep 0.1s
cd home
sleep 0.2s
read -p "Please Enter Your EXACT Username:  " user
sleep 0.2s
cd user
echo "\n"
sleep 1s
echo "This Will Download SPP To Your Device"
read -p "Type 'YES' To Continue:  " confirm
echo "\n"
if [ confirm == "YES" ]; then
echo "Starting 1st Download...."
sleep 3s
echo "Downloading #1...."
wget -tries=15 https://raw.githubusercontent.com/Albie737/SimplePicoPython/main/SPP-Setup.py
sleep 1s
echo "Finished #1"
echo "Starting 2nd Download...."
sleep 3s
echo "Downloading #2...."
wget -tries=15 https://raw.githubusercontent.com/Albie737/SimplePicoPython/main/main.py
sleep 1s
echo "Finished #2"
sleep 2s
echo "Finalising All Downloads"
sleep 5s
echo "Finished!"
sleep 0.5s
echo "Your Files Should Be Located In Your Account's 'Home' Folder"
sleep 0.5s
echo "\n"
echo "End Of Script"
elif [ confirm == "yes" ]; then
echo "ERROR: User has Not Confirmed\nTry All Caps"
sleep 0.5s
echo "\n"
echo "End Of Script"
elif [ confirm == "Yes" ]; then
echo "ERROR: User has Not Confirmed\nTry All Caps"
sleep 0.5s
echo "\n"
echo "End Of Script"
elif [ confirm == "yES" ]; then
echo "ERROR: User has Not Confirmed\nTry All Caps"
sleep 0.5s
echo "\n"
echo "End Of Script"
else
echo "ERROR: An Unknown Input Has (Possibly) Been Entered"
sleep 0.5s
echo "\n"
echo "End Of Script"
fi