from flack import Flack
import os
import smtplib
from email.mime.text import MIMEtext
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

# No authentication for disposable email
SMTP_USER = None
SMTP_PASSWORD = None

# Thresholds (using environment variables)
CPU_THRESHOLD = float(os.getenv('CPU_THRESHOLD', 80.0))
MEMORY_THRESHOLD = int(os.getenv('MEMORY_THRESHOLD', 3024))

# Log file path
LOG_FILE_PATH = os.path.expanduser(os.getenv("~/Desktop/all_data.log"))


# SMTP settings (using environment variables)
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 25))
FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')

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
                if cpu_usage > CPU_THRESHOLD:
                    send_email(f"High Memory Usage at {timestamp}", f"Memory usage: {memory_usage} MB")
            except ValueError:
                continue
    

    #Checks if the script is being run directly (not imported as a module)
    if __name__ == "__main__":
    analyze_log()
