from flask import Flask
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Thresholds (using environment variables with defaults)
CPU_THRESHOLD = float(os.getenv('CPU_THRESHOLD', 80.0))
MEMORY_THRESHOLD = int(os.getenv('MEMORY_THRESHOLD', 3024))

# Log file path (expanduser does not work with an environment variable)
LOG_FILE_PATH = os.path.expanduser(os.getenv('LOG_FILE_PATH', "~/Desktop/all_data.log"))

# SMTP settings (using environment variables)
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 25))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')

# Initialize Flask application
app = Flask(__name__)

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

@app.route('/')
def index():
    return 'Server is running!'

@app.route('/analyze')
def analyze():
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            try:
                timestamp, cpu, mem = line.split(", ")
                cpu_usage = float(cpu.split(": ")[1].replace('%', ''))
                memory_usage = int(mem.split(": ")[1].replace(' MB', ''))
                if cpu_usage > CPU_THRESHOLD:
                    send_email(f"High CPU Usage at {timestamp}", f"CPU usage: {cpu_usage}%")
                if memory_usage > MEMORY_THRESHOLD:
                    send_email(f"High Memory Usage at {timestamp}", f"Memory usage: {memory_usage} MB")
            except ValueError:
                continue

    return 'Analysis complete.'

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
