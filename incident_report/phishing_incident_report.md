# Phishing Incident Investigation Report

## Incident Summary
Multiple users attempted to access suspicious phishing domains detected through simulated Zscaler Internet Access (ZIA) logs monitored in Splunk SIEM.

## Detection Source
Splunk dashboards and SPL detection queries identified repeated blocked requests to phishing-related domains.

## Affected Users
- akshaya
- mike
- priya
- david
- john
- sarah

## Indicators of Compromise (IOCs)
- phishing-login.com
- unknown-domain.xyz
- malware-download.net

## Detection Queries

```spl
index=zscaler threat_type=phishing
```

```spl
index=zscaler action=blocked
| stats count by user
```

## Security Actions Taken
- Blocked suspicious domains through URL filtering policies
- Investigated user access attempts
- Monitored phishing activity using Splunk dashboards
- Performed log analysis for suspicious traffic patterns

## Recommendations
- Improve phishing awareness training
- Expand SSL inspection policies
- Monitor repeated malicious access attempts
- Implement automated SIEM alerting

## Outcome
Threat activity was successfully identified and monitored through Splunk SIEM dashboards and simulated Zscaler security controls.
