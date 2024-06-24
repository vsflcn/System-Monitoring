import os
import smtplib
from email.mime.text import MIMEtext
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

# Thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 3024  # in MB
