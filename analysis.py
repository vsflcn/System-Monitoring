import os
import smtplib
from email.mime.text import MIMEtext
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

# Thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 3024  # in MB

# Log file path
LOG_FILE_PATH = os.path.expanduser("~/Desktop/all_data.log")

def send_email(subject, message):
    msg = MIMEtext(message)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

def analize()
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            try:
                timestamp, cpu, mem = line.split(", ")
                cpu_usage = float(cpu.split(": ")[1].replace('%', ''))
                memory_usage = int(mem.split(": ")[1].replace(' MB', ''))