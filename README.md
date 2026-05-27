# Zscaler SASE Security Operations Lab

## Overview
This project simulates a Zscaler Internet Access (ZIA) and Splunk SIEM security operations environment using Ubuntu, Python, and Splunk Enterprise.

The lab demonstrates:
- SASE and Zero Trust concepts
- URL filtering and web security policies
- Simulated ZIA web traffic logs
- Splunk SIEM ingestion and monitoring
- Phishing detection workflows
- Security dashboarding and analytics



## Technologies Used
- Ubuntu 24.04
- Splunk Enterprise
- Python 3
- GitHub
- Zscaler Internet Access (ZIA) concepts
- SIEM Monitoring
- SASE Security Architecture


## Features
- Simulated enterprise web traffic
- URL filtering policy implementation
- Phishing and suspicious domain detections
- Splunk dashboards for SOC monitoring
- User activity analysis
- Threat monitoring workflows



## Dashboard Visualizations
The project includes:
- Phishing Attempts by User
- Blocked Traffic by Category
- Top Accessed Domains
- Users with Most Blocked Activity

Dashboard export available in:
```text
screenshots/zscaler_security_operations_dashboard-2026-05-27.pdf
```



## Detection Queries

### Phishing Attempts
```spl
index=zscaler threat_type=phishing
| stats count by user
```

### Blocked Traffic
```spl
index=zscaler action=blocked
| stats count by category
```

### Top Domains
```spl
index=zscaler
| stats count by url
| sort -count
```

---

## Project Structure

```text
architecture/
dashboards/
incident_report/
logs/
policies/
scripts/
screenshots/
README.md
```



## Learning Outcomes
This project helped develop hands-on experience with:
- SIEM operations
- Log analysis
- Security monitoring
- Dashboard creation
- Splunk SPL queries
- SASE architecture concepts
- Threat detection workflows



## Author
Akshaya Konduru
