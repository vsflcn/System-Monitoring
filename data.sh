#!/bin/bash
#This script will monitor data about CPU and memory usage on Linux Ubuntu VM and collect it in the all_data.log file

while :
do
    #Current CPU & memory usage state
    cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}') # top command provides dynamic state of working OS in real time 
    memUsage=$(free -m | awk '/Mem/{print $3}') #free command shows total amount of free and used physical and swap memory on the system