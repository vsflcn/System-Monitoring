# System Monitoring with Notifications

This project implements a system monitoring solution for tracking system metrics (CPU, memory) using Bash scripts for data collection and Python for analysis and alert notifications via email.

## Skills Utilized
- Data Collection
- Bash Scripting
- Python
- API Integration

## Description

The project consists of two main components:

1. **Bash scripts for data collection:**
   - The `data.sh` script collects CPU load & memory usage data using `top`and `free` utilities.
   - Data is logged into the `all_data.log` file.

2. **Python script for analysis and notifications:**
   - The `analysis.py` script reads data from `all_data.log`, analyzes it, and sends notifications if values exceed predefined thresholds.
   - Notifications can be sent via email.

## Usage

- The container will continuously monitor system performance.
- Alerts are sent via email if CPU or memory usage exceeds thresholds.
- Use the web interface to access logs or shut down the server.
