import csv
import random
from datetime import datetime, timedelta

users = ["akshaya", "john", "sarah", "mike", "priya", "david"]

urls = [
    ("github.com", "allowed", "none", "development"),
    ("office.com", "allowed", "none", "business"),
    ("phishing-login.com", "blocked", "phishing", "security-risk"),
    ("malware-download.net", "blocked", "malware", "security-risk"),
    ("dropbox.com", "allowed", "none", "cloud-storage"),
    ("gambling-site.com", "blocked", "policy_violation", "gambling"),
    ("unknown-domain.xyz", "blocked", "suspicious", "unknown")
]

start_time = datetime.now() - timedelta(days=7)

with open("../logs/zscaler_web_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "user", "source_ip", "url", "action", "threat_type", "category", "bytes"])

    for i in range(500):
        timestamp = start_time + timedelta(minutes=i * 10)
        user = random.choice(users)
        source_ip = f"10.0.0.{random.randint(10,250)}"
        url, action, threat_type, category = random.choice(urls)
        bytes_used = random.randint(1000,500000)

        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            user,
            source_ip,
            url,
            action,
            threat_type,
            category,
            bytes_used
        ])

print("Generated zscaler_web_logs.csv")
