#!/bin/bash
#This script will monitor data about CPU and memory usage on Linux Ubuntu VM and collect it in the all_data.log file

while :
do
    #Current CPU & memory usage state
    cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}') 