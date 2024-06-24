#!/bin/bash
#This script will monitor data about CPU and memory usage on Linux Ubuntu VM and collect it in the all_data.log file

#Getting the current time
timeatamp=$(date '+%Y-%m-%d %H:%M:%S')

while :
do
    #Current CPU & memory usage state
    cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}') # top command provides dynamic state of working OS in real time 
    memUsage=$(free -m | awk '/Mem/{print $3}') #free command shows total amount of free and used physical and swap memory on the system

    #Print the usage
    echo "Cpu Usage: $cpuUsage%"
    echo "Memory usage: $memUsage MB"

    echo "$timestamp, CPU usage: $cpuUsage%, Memory Usage: $memUsage MB" >> /HOME/Desktop/all_data.log"

    #Sleep for 1 second
    sleep 1
done 


